class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c]=="0" or grid[r][c]=="2":
                return
            
            grid[r][c] = "2"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1":
                    dfs(r, c)
                    count+=1
        
        return count
