class Solution:
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    def arraySign(self, nums: List[int]) -> int:
        product = math.prod(nums)  # Compute product of all elements
        return self.signFunc(product)  # Call the signFunc method
