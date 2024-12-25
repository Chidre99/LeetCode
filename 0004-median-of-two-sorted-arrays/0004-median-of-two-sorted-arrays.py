class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        merged = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i = i+1
            else:
                merged.append(nums2[j])
                j = j+1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        return statistics.median(merged) 