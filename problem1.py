class ProductionOptimization:
    def __init__(self):
        pass

    def optimize_production(self, durations: list[int], stations: int) -> int:
	    #we will define the lower bound and the higher bound to find the longest station
        #the longest duration of the single station can be between the longest_durations of a single station to the total summation of all durations in the Durations[] array.

        lower_bound = max(durations)
        upper_bound = sum(durations)
        
        #define the result to return the longest duration
        result = float("inf")

        #Optimize using binary search. In between the lower bound and the higher bound, we calculate the longest_estimate_value to be the middle of the lower bound and higher bound. 
        while lower_bound <= upper_bound:
            middle_point = lower_bound + ((upper_bound - lower_bound) // 2)
            
            #we check if we can divide stations further by estimating if the can_divide() is in the lower half or the upper half of values between the lower_bound and the higher_bound.
            #if we can continue to divide then the solution is in the lower half , we reduce the higher_bound by half.
            if self.can_divide(middle_point, durations, stations):
                result = middle_point
                upper_bound = middle_point - 1
            #if not we increase the lower_bound because we know the solution will be in the upper half between the lower bound and the higher bound.
            else:
                lower_bound = middle_point + 1
        return result

    #checking if the line can be optimized. A line can be optimized if the duration of the current station is less than the longest_estimate_value.
    def can_divide(self, longest_estimate: int, durations: list[int], stations: int) -> bool:
        num_stations = 1    #initiate the number of stations
        duration_current_station = 0 #initiate the duration of the current station

        for duration in durations:
            if duration_current_station + duration <= longest_estimate:
                duration_current_station += duration
            else:
                num_stations += 1 # we increment the number_of_station to indicate this is the longest duration we could estimate for 1 station and continue to the next station.
                duration_current_station = duration
                #after greedily separating the stations, we want to return to the function can_divide by checking if the number_of_station is greater than our input stations.
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