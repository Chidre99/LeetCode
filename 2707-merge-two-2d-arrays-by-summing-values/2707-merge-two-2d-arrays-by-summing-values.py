class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        merged = defaultdict(int)
        for id, value in nums1:
            merged[id] += value
        for id, value in nums2:
            merged[id] += value
        return sorted([[id, value] for id, value in merged.items()])
