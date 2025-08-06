from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.data = [0] * (2 * self.size)
        for i, v in enumerate(nums):
            self.data[self.size + i] = v
        for i in range(self.size - 1, 0, -1):
            self.data[i] = max(self.data[i << 1], self.data[i << 1 | 1])

    def _update_to_minus_one(self, idx: int) -> None:
        pos = idx + self.size
        self.data[pos] = -1
        pos >>= 1
        while pos:
            self.data[pos] = max(self.data[pos << 1], self.data[pos << 1 | 1])
            pos >>= 1

    def take_leftmost_ge(self, need: int) -> int:
        if self.data[1] < need:
            return -1
        node = 1
        while node < self.size:
            left = node << 1
            node = left if self.data[left] >= need else left | 1
        idx = node - self.size
        self._update_to_minus_one(idx)
        return idx

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(baskets)
        unplaced = 0
        for qty in fruits:
            if seg.take_leftmost_ge(qty) == -1:
                unplaced += 1
        return unplaced
