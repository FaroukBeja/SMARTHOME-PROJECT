import json
import os
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta
from typing import List, Optional

STORAGE_FILE = "rent_reminders.json"


@dataclass
class RentReminder:
    tenant_name: str
    amount: float
    due_date: str
    note: str = ""

    def due_date_obj(self) -> date:
        return datetime.strptime(self.due_date, "%Y-%m-%d").date()

    def days_until_due(self, reference: Optional[date] = None) -> int:
        if reference is None:
            reference = date.today()
        return (self.due_date_obj() - reference).days

    def status(self, reference: Optional[date] = None) -> str:
        days_left = self.days_until_due(reference)
        if days_left < 0:
            return "Overdue"
        if days_left == 0:
            return "Due today"
        return f"Due in {days_left} day(s)"

    def to_dict(self) -> dict:
        return asdict(self)


class RentReminderSystem:
    def __init__(self, storage_file: str = STORAGE_FILE):
        self.storage_file = storage_file
        self.reminders: List[RentReminder] = []
        self.load_reminders()

    def load_reminders(self) -> None:
        if not os.path.exists(self.storage_file):
            self.reminders = []
            return
        with open(self.storage_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        self.reminders = [RentReminder(**item) for item in data]

    def save_reminders(self) -> None:
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([reminder.to_dict() for reminder in self.reminders], file, indent=2)

    def add_reminder(self, tenant_name: str, amount: float, due_date: str, note: str = "") -> None:
        reminder = RentReminder(tenant_name=tenant_name, amount=amount, due_date=due_date, note=note)
        self.reminders.append(reminder)
        self.save_reminders()

    def remove_reminder(self, tenant_name: str) -> bool:
        original_count = len(self.reminders)
        self.reminders = [reminder for reminder in self.reminders if reminder.tenant_name != tenant_name]
        if len(self.reminders) < original_count:
            self.save_reminders()
            return True
        return False

    def due_reminders(self, within_days: int = 7, reference: Optional[date] = None) -> List[RentReminder]:
        if reference is None:
            reference = date.today()
        return [reminder for reminder in self.reminders if 0 <= reminder.days_until_due(reference) <= within_days]

    def overdue_reminders(self, reference: Optional[date] = None) -> List[RentReminder]:
        if reference is None:
            reference = date.today()
        return [reminder for reminder in self.reminders if reminder.days_until_due(reference) < 0]

    def all_reminders(self) -> List[RentReminder]:
        return sorted(self.reminders, key=lambda r: r.due_date_obj())


def format_reminder(reminder: RentReminder) -> str:
    return f"{reminder.tenant_name}: {reminder.amount:.2f} due {reminder.due_date} ({reminder.status()}) {reminder.note}"


def print_reminders(reminders: List[RentReminder], heading: str) -> None:
    print(heading)
    if not reminders:
        print("  None")
        return
    for reminder in reminders:
        print("  -", format_reminder(reminder))


def print_help() -> None:
    print("Rent Reminder System")
    print("Usage:")
    print("  python rrs.py list")
    print("  python rrs.py due [days]")
    print("  python rrs.py overdue")
    print("  python rrs.py add <tenant_name> <amount> <due_date YYYY-MM-DD> [note]")
    print("  python rrs.py remove <tenant_name>")


def main() -> None:
    import sys

    system = RentReminderSystem()
    args = sys.argv[1:]

    if not args:
        print_help()
        return

    command = args[0].lower()

    if command == "list":
        print_reminders(system.all_reminders(), "All rent reminders:")
    elif command == "due":
        days = int(args[1]) if len(args) > 1 else 7
        print_reminders(system.due_reminders(within_days=days), f"Reminders due in the next {days} day(s):")
    elif command == "overdue":
        print_reminders(system.overdue_reminders(), "Overdue rent reminders:")
    elif command == "add" and len(args) >= 4:
        tenant_name = args[1]
        amount = float(args[2])
        due_date = args[3]
        note = " ".join(args[4:]) if len(args) > 4 else ""
        system.add_reminder(tenant_name, amount, due_date, note)
        print(f"Added reminder for {tenant_name}.")
    elif command == "remove" and len(args) == 2:
        tenant_name = args[1]
        if system.remove_reminder(tenant_name):
            print(f"Removed reminder for {tenant_name}.")
        else:
            print(f"No reminder found for {tenant_name}.")
    else:
        print_help()


if __name__ == "__main__":
    main()
