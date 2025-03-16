class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node: int):
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                province_count += 1

        return province_count
