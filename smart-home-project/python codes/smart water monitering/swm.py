from datetime import datetime

    
class SmartWaterMonitor:
    """Monitor tank water levels, low-water alerts, and usage statistics."""

    def __init__(self, capacity_liters, current_level_liters=0):
        if capacity_liters <= 0:
            raise ValueError("Capacity must be a positive number.")
        self.capacity = float(capacity_liters)
        self.current_level = min(max(float(current_level_liters), 0.0), self.capacity)
        self.total_consumed = 0.0
        self.usage_history = []

    def add_water(self, liters):
        liters = float(liters)
        if liters < 0:
            raise ValueError("Cannot add a negative amount of water.")
        self.current_level = min(self.capacity, self.current_level + liters)
        return self.current_level

    def use_water(self, liters):
        liters = float(liters)
        if liters < 0:
            raise ValueError("Cannot use a negative amount of water.")
        if liters > self.current_level:
            liters = self.current_level
        self.current_level -= liters
        self.total_consumed += liters
        self.usage_history.append({
            "timestamp": datetime.now(),
            "amount_liters": liters,
        })
        return liters

    def level_percentage(self):
        return (self.current_level / self.capacity) * 100.0

    def is_low(self, threshold_percent=20.0):
        return self.level_percentage() <= float(threshold_percent)

    def usage_statistics(self):
        count = len(self.usage_history)
        average = self.total_consumed / count if count else 0.0
        return {
            "capacity_liters": self.capacity,
            "current_level_liters": self.current_level,
            "level_percent": round(self.level_percentage(), 2),
            "total_consumed_liters": round(self.total_consumed, 2),
            "events": count,
            "average_usage_per_event_liters": round(average, 2),
        }

    def low_water_alert(self, threshold_percent=20.0):
        if self.is_low(threshold_percent):
            return f"Alert: water level is low ({self.level_percentage():.1f}% remaining)."
        return f"Water level is sufficient ({self.level_percentage():.1f}% remaining)."


if __name__ == "__main__":
    tank = SmartWaterMonitor(capacity_liters=1000, current_level_liters=650)
    print(tank.low_water_alert())

    tank.use_water(120)
    tank.use_water(80)
    tank.use_water(450)
    tank.add_water(300)

    print("Current level:", f"{tank.current_level:.1f} L")
    print("Level percent:", f"{tank.level_percentage():.1f}%")
    print(tank.low_water_alert(threshold_percent=30))
    print("Usage stats:", tank.usage_statistics())
