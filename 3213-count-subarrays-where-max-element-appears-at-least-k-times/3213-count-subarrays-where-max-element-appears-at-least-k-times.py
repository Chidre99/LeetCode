class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        ans= 0
        max_elements_in_window = 0
        max_element = max(nums)
        size = len(nums)
        for j in range(size):
            if nums[j] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[i] == max_element:
                    max_elements_in_window -=1
                i +=1
            ans += i
        return ans
            