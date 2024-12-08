class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events based on their end times
        events.sort(key=lambda x: x[1])
        
        # Keep track of the maximum value of a single event
        max_single = 0
        result = 0
        
        # List to store the maximum values encountered so far
        max_values = []
        end_times = []
        
        for start, end, value in events:
            # Use binary search to find the latest non-overlapping event
            idx = bisect_right(end_times, start - 1) - 1
            
            # If there's a valid non-overlapping event, update result
            if idx >= 0:
                result = max(result, max_values[idx] + value)
            
            # Also consider the current event alone
            result = max(result, value)
            
            # Update max_single and append to max_values and end_times
            max_single = max(max_single, value)
            max_values.append(max_single)
            end_times.append(end)
        
        return result
        