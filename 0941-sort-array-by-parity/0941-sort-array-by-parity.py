class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        odd=[]
        even = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even+odd