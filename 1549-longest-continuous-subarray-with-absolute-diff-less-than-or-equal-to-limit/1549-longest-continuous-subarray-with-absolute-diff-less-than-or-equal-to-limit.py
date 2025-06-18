class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        res = 0

        for right, num in enumerate(nums):
            while maxDeque and num > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(num)

            while minDeque and num < minDeque[-1]:
                minDeque.pop()
            minDeque.append(num)

            while maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[left]:
                    maxDeque.popleft()
                if minDeque[0] == nums[left]:
                    minDeque.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res
