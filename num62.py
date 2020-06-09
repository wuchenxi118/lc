class Solution:
    # def __init__(self):
    #     self.res = 0
    # def uniquePaths(self, m, n):
    #     self._dfs(0, 0, m-1, n-1)
    #     return self.res
    #
    #
    #
    # def _dfs(self,now_m,now_n,m,n):
    #     if now_m==m and now_n==n:
    #         self.res+=1
    #         return
    #     if now_m>m or now_n>n:
    #         return
    #
    #     self._dfs(now_m+1,now_n,m,n)
    #
    #     self._dfs(now_m,now_n+1,m,n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

















if __name__ == '__main__':
    m = 5
    n = 4

    S = Solution()
    print(S.uniquePaths(m,n))