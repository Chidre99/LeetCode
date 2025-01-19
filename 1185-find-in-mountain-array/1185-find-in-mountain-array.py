class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary_search(start, end, target, is_asc):
            while start <= end:
                mid = (start + end) // 2
                value = mountainArr.get(mid)
                if value == target:
                    return mid
                if is_asc:
                    if value < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if value > target:
                        start = mid + 1
                    else:
                        end = mid - 1
            return -1

        # Step 1: Find the peak index
        left, right = 0, mountainArr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # Step 2: Binary search in the ascending part
        index = binary_search(0, peak, target, True)
        if index != -1:
            return index

        # Step 3: Binary search in the descending part
        return binary_search(peak + 1, mountainArr.length() - 1, target, False)
