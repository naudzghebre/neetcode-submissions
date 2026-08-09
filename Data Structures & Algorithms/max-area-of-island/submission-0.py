class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIsland = 0

        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c) -> int:

            if min(r,c) <  0 or r == ROW or c == COL or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxIsland = max(maxIsland, area)
        return maxIsland
