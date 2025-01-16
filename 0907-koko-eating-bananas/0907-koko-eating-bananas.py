class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize binary search boundaries
        left, right = 1, max(piles)

        # Helper function to check if a given speed is valid
        def can_finish(speed):
            total_hours = 0
            for pile in piles:
                
                total_hours += -(-pile // speed)  
            return total_hours <= h

        # Binary search
        while left < right:
            middle = (left + right) // 2
            if can_finish(middle):
                right = middle  
            else:
                left = middle + 1  

        return left
