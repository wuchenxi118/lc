class Solution:
    def __init__(self):
        self.res=0
    def findTargetSumWays(self, nums, S):
        self.calculate(nums,0,0,S)
        return self.res


    def calculate(self,nums,i,n_sum,S):
        if i==len(nums):
            if n_sum == S:
                self.res+=1
        else:
            self.calculate(nums,i+1,n_sum+nums[i],S)
            self.calculate(nums,i+1,n_sum-nums[i],S)


if __name__ == '__main__':
    inp = [1, 1, 1, 1, 1]
    S = 3
    So = Solution()
    print(So.findTargetSumWays(inp,S))

