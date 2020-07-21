class Solution:
    def lengthOfLIS(self, nums):
        Len = len(nums)

        if Len<2:
            return Len

        dp = [1] * Len

        for i in range(1,Len):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)

        res = 0
        for x in dp:
            res = max(res,x)

        return res
