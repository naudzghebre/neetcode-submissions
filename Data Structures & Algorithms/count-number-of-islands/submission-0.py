class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):

            if min(r,c) <  0 or r == ROW or c == COL or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands


        

