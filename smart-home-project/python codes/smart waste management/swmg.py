"""Module 3: Smart Waste Management
Monitor bin capacity and trigger collection alerts.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class WasteBin:
    id: str
    capacity_percent: float
    location: str = ""

    def needs_collection(self, threshold: float = 80.0) -> bool:
        return self.capacity_percent >= threshold


def generate_alerts(bins: List[WasteBin], threshold: float = 80.0) -> List[str]:
    alerts = []
    for bin in bins:
        if bin.needs_collection(threshold):
            alerts.append(
                f"Alert: Bin {bin.id} at {bin.location or 'unknown location'} "
                f"is {bin.capacity_percent:.1f}% full and needs collection."
            )
    return alerts


def monitor_bins(bins: List[WasteBin], threshold: float = 80.0) -> None:
    alerts = generate_alerts(bins, threshold)
    if not alerts:
        print("All bins are below threshold. No collection alerts.")
    else:
        for alert in alerts:
            print(alert)


def main() -> None:
    sample_bins = [
        WasteBin(id="B1", capacity_percent=45.0, location="Main Street"),
        WasteBin(id="B2", capacity_percent=82.5, location="Park Entrance"),
        WasteBin(id="B3", capacity_percent=91.0, location="Shopping Plaza"),
        WasteBin(id="B4", capacity_percent=76.0, location="Library"),
    ]

    monitor_bins(sample_bins)


if __name__ == "__main__":
    main()
