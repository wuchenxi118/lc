class Solution:
    def numIslands(self, grid):
        nr = len(grid)
        if nr==0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    num_islands+=1
                    self.dfs(grid,r,c,nr,nc)

        return num_islands

    def dfs(self,grid,r,c,nr,nc):
        grid[r][c]=0
        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y]=='1':
                self.dfs(grid,x,y,nr,nc)
