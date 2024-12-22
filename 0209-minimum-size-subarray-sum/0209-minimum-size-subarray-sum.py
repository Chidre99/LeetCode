class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        current_sum = 0
        count = 0
        result = float('inf')
        size = len(nums)
        while j <size:
            current_sum =current_sum + nums[j]
            while current_sum >= target:
                result = min(result,j-i+1) 
                current_sum -= nums[i]
                i+=1
            j = j+1
        return 0 if result == float('inf') else result