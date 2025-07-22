class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]

        expectedSum = n * (n+1) // 2
        actualSum = sum(abs(num) for num in nums)
        duplicatedNumber = result[0]
        missing_number = expectedSum - (actualSum - duplicatedNumber)
        result.append(abs(missing_number))
        return result     
        
        
        