class Production_Optimization:
    def __init__(self) -> None:
        
    def Production_Optimization(self, Durations: list[int], stations: int) -> int:
        lower_bound = max(Durations)
        higher_bound = sum(Durations)
        result = float("inf")
        
        while lower_bound <= higher_bound:
            middle_point = lower_bound + ((higher_bound - lower_bound) // 2) 
            if self.can_divide(middle_point, Durations, stations):
                result = middle_point
                higher_bound = middle_point - 1
            else:
                lower_bound = middle_point + 1
        return result
    
    def can_divide(self, longest_estimate_value: int, Durations: list[int], stations: int):
        number_of_station = 0
        duration_of_current_station = 0
        for duration in Durations:
            duration_of_current_station += duration
            if duration_of_current_station >= longest_estimate_value:
                number_of_station += 1
                duration_of_current_station = duration
        return number_of_station + 1 <= stations 