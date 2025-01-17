class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_load = sum(weights)
        max_load = max(weights)

        def feasible(weights,capacity,days):
            current_load = 0
            required_days = 1
            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = weight
                    if required_days > days:
                        return False
                else:
                    current_load += weight
            return True



        l = max_load
        r = total_load
        while l < r:
            mid =  l +(r-l)//2
            if feasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1
        return l

