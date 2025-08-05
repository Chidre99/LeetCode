from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        tree = [-1] * (2 * size)
        for i, cap in enumerate(baskets):
            tree[size + i] = cap
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[i << 1], tree[i << 1 | 1])

        def update(pos: int) -> None:
            idx = pos + size
            tree[idx] = -1
            idx >>= 1
            while idx:
                tree[idx] = max(tree[idx << 1], tree[idx << 1 | 1])
                idx >>= 1

        def first_ge(target: int) -> int:
            if tree[1] < target:
                return -1
            idx = 1
            while idx < size:
                left = idx << 1
                idx = left if tree[left] >= target else left | 1
            return idx - size

        unplaced = 0
        for amt in fruits:
            pos = first_ge(amt)
            if pos == -1:
                unplaced += 1
            else:
                update(pos)
        return unplaced
