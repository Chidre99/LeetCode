class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen elements
        seen = set()
        
        # Iterate through the list
        for num in nums:
            # If the number is already in the set, it's a duplicate
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If no duplicates are found, return False
        return False
