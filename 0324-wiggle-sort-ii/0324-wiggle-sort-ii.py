class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        import random

        def nth_element(nums, n):
            def select(left, right, n):
                pivot = nums[random.randint(left, right)]
                l, m, r = left, left, right
                while m <= r:
                    if nums[m] < pivot:
                        nums[l], nums[m] = nums[m], nums[l]
                        l += 1
                        m += 1
                    elif nums[m] > pivot:
                        nums[m], nums[r] = nums[r], nums[m]
                        r -= 1
                    else:
                        m += 1
                if n < l:
                    return select(left, l - 1, n)
                elif n > r:
                    return select(r + 1, right, n)
                else:
                    return nums[n]

            return select(0, len(nums) - 1, n)

        n = len(nums)
        median = nth_element(nums[:], n // 2)

        def virtual_index(i):
            return (1 + 2 * i) % (n | 1)

        # Three-way partition using Dutch National Flag
        left, i, right = 0, 0, n - 1
        while i <= right:
            vi = virtual_index(i)
            if nums[vi] > median:
                nums[virtual_index(left)], nums[vi] = nums[vi], nums[virtual_index(left)]
                left += 1
                i += 1
            elif nums[vi] < median:
                nums[vi], nums[virtual_index(right)] = nums[virtual_index(right)], nums[vi]
                right -= 1
            else:
                i += 1
