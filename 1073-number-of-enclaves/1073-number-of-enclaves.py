class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid), len(grid[0])


        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][cols-1] == 1:
                dfs(i,cols-1)

        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[rows-1][j] == 1:
                dfs(rows-1,j)


        count = 0
        for row in grid:
            count += row.count(1)

        return count