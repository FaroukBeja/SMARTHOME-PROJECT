"""Smart Energy Monitoring

Simulate appliance usage and calculate electricity consumption.
"""

from typing import Dict, Tuple

APPLIANCES = {
    "LED Bulb": 10,          # watts
    "Ceiling Fan": 70,       # watts
    "Refrigerator": 150,     # watts
    "Laptop": 65,            # watts
    "Washing Machine": 500,  # watts
    "Air Conditioner": 1200, # watts
}

COST_PER_KWH = 0.16  # currency units per kilowatt-hour


def calculate_energy_kwh(wattage: float, hours: float) -> float:
    """Return energy consumption in kilowatt-hours."""
    return (wattage * hours) / 1000.0


def calculate_cost(kwh: float, rate: float = COST_PER_KWH) -> float:
    """Return cost for the given energy consumption."""
    return round(kwh * rate, 2)


def simulate_usage(usage_hours: Dict[str, float]) -> Tuple[float, Dict[str, float]]:
    """Simulate appliance usage and return total energy and breakdown."""
    breakdown = {}
    total_kwh = 0.0

    for appliance, hours in usage_hours.items():
        wattage = APPLIANCES.get(appliance)
        if wattage is None:
            raise ValueError(f"Unknown appliance: {appliance}")
        energy = calculate_energy_kwh(wattage, hours)
        breakdown[appliance] = round(energy, 3)
        total_kwh += energy

    return round(total_kwh, 3), breakdown


def print_report(usage_hours: Dict[str, float]) -> None:
    total_kwh, breakdown = simulate_usage(usage_hours)
    total_cost = calculate_cost(total_kwh)

    print("Smart Energy Monitoring Report")
    print("-------------------------------")
    for appliance, energy in breakdown.items():
        print(f"{appliance}: {energy} kWh")
    print("-------------------------------")
    print(f"Total consumption: {total_kwh} kWh")
    print(f"Estimated cost: {total_cost} currency units")


if __name__ == "__main__":
    example_usage = {
        "LED Bulb": 5.0,
        "Ceiling Fan": 8.0,
        "Refrigerator": 24.0,
        "Laptop": 4.0,
        "Washing Machine": 1.5,
        "Air Conditioner": 6.0,
    }
    print_report(example_usage)
