class ProductionOptimization:
    def __init__(self):
        pass

    def optimize_production(self, durations: list[int], stations: int) -> int:
        lower_bound = max(durations)
        upper_bound = sum(durations)
        result = float("inf")

        while lower_bound <= upper_bound:
            middle_point = lower_bound + ((upper_bound - lower_bound) // 2)
            if self.can_divide(middle_point, durations, stations):
                result = middle_point
                upper_bound = middle_point - 1
            else:
                lower_bound = middle_point + 1
        return result

    def can_divide(self, longest_estimate: int, durations: list[int], stations: int) -> bool:
        num_stations = 1
        duration_current_station = 0

        for duration in durations:
            if duration_current_station + duration <= longest_estimate:
                duration_current_station += duration
            else:
                num_stations += 1
                duration_current_station = duration
                if num_stations > stations:
                    return False
        return True

def main():
    optimizer = ProductionOptimization()
    durations = [15, 15, 30, 30, 45]  # Example durations
    stations = 3  # Example number of stations
    result = optimizer.optimize_production(durations, stations)
    print("Longest duration of a single station in the assembly line after optimizing the line is:", result)

if __name__ == "__main__":
    main()