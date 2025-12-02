class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j = 0,0
        ans_list = []
        s = set()
        nums1.sort()
        nums2.sort()
        while i <len(nums1):
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    s.add(nums2[j])
                    break
                elif nums2[j] > nums1[i]:
                    break
                j +=1
            i +=1
        return sorted(s)