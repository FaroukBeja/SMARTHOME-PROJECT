import json
import os
import uuid
from datetime import datetime

DATA_FILE = "visitor_history.json"


def load_history():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_history(history):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2, ensure_ascii=False)


def generate_entry_pass(visitor):
    pass_text = (
        f"Visitor Entry Pass\n"
        f"-------------------\n"
        f"Pass ID: {visitor['pass_id']}\n"
        f"Name: {visitor['name']}\n"
        f"Company: {visitor['company']}\n"
        f"Contact: {visitor['contact']}\n"
        f"Purpose: {visitor['purpose']}\n"
        f"Check-in: {visitor['check_in']}\n"
        f"Expected departure: {visitor['expected_departure']}\n"
    )
    return pass_text


def register_visitor():
    name = input("Visitor name: ").strip()
    company = input("Company/Organization: ").strip()
    contact = input("Contact number or email: ").strip()
    purpose = input("Purpose of visit: ").strip()
    expected_departure = input("Expected departure time (optional): ").strip()

    if not name or not contact or not purpose:
        print("Name, contact, and purpose are required.")
        return

    visitor = {
        "pass_id": str(uuid.uuid4()),
        "name": name,
        "company": company,
        "contact": contact,
        "purpose": purpose,
        "check_in": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "expected_departure": expected_departure or "Not specified",
    }

    history = load_history()
    history.append(visitor)
    save_history(history)

    print("\nEntry pass generated:\n")
    print(generate_entry_pass(visitor))


def view_history():
    history = load_history()
    if not history:
        print("No visitor records found.")
        return

    for visitor in history:
        print("-----------------------------")
        print(generate_entry_pass(visitor))


def main():
    while True:
        print("\nSmart Visitor Management")
        print("1. Register visitor")
        print("2. View visit history")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register_visitor()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
