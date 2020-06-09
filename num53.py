class Solution:
    def maxSubArray(self, nums):
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre+x,x)
            maxAns = max(maxAns,pre)
        return maxAns