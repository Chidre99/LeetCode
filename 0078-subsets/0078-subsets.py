class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
    
        first, rest = nums[0], nums[1:]
        subsets_without_first = self.subsets(rest)
        subsets_with_first = [subset + [first] for subset in subsets_without_first]
    
        return subsets_without_first + subsets_with_first