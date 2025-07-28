class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, visited):
            nonlocal count
            if pos > n:
                count += 1
                return
            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    backtrack(pos + 1, visited)
                    visited[num] = False

        count = 0
        visited = [False] * (n + 1)  # 1-based indexing
        backtrack(1, visited)
        return count
