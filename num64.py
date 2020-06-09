class Solution:
    def minPathSum(self, grid) -> int:
        return self.calculate(grid,0,0)


    def calculate(self,grid,i,j):
        if i==len(grid) or j==len(grid[0]):
            return float('inf')
        if i==len(grid)-1 and j==len(grid[0])-1:
            return grid[i][j]
        return grid[i][j]+min(self.calculate(grid,i+1,j),self.calculate(grid,i,j+1))



if __name__ == '__main__':
    inp = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

    S = Solution()
    print(S.minPathSum(inp))
