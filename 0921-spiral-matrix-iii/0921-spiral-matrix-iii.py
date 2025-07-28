class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        r, c = rStart, cStart
        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        while len(result) < rows * cols:
            for d in range(4):
                dr, dc = dirs[d]
                for _ in range(steps if d % 2 == 0 else steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r += dr
                    c += dc
                if d % 2 == 1:
                    steps += 1  # increase step size after every two directions
        return result
