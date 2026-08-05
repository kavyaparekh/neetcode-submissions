class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if r == -1 or r >= R or c == -1 or c >= C or grid[r][c] == '0' or grid[r][c] == '2':
                return

            grid[r][c] = '2'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        
        return res