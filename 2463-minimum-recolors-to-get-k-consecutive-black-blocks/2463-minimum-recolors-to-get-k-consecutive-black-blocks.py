class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = float('inf')
        white = 0
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                white += 1
            if i >= k:
                if blocks[i - k] == 'W':
                    white -= 1
            if i >= k - 1:
                min_recolor = min(min_recolor, white)
        return min_recolor
