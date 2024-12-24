class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Count the occurrences of each number using a hash map
        counts = Counter(nums)
        
        # Step 2: Find the threshold for majority
        n = len(nums)
        threshold = n // 3
        
        # Step 3: Collect elements that appear more than n/3 times
        result = [num for num, count in counts.items() if count > threshold]
        
        return result
