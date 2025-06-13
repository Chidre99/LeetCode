class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        target_indices = {val: i for i, val in enumerate(target)}
        

        subsequence = []
        for num in arr:
            if num in target_indices:
                subsequence.append(target_indices[num])
        
        def lengthOfLIS(nums):
            if not nums:
                return 0
            
            dp = []
            for num in nums:
                left, right = 0, len(dp)
                while left < right:
                    mid = (left + right) // 2
                    if dp[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                
                if left == len(dp):
                    dp.append(num)
                else:
                    dp[left] = num
            
            return len(dp)
        
        lcs_length = lengthOfLIS(subsequence)
        return len(target) - lcs_length