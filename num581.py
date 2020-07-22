class Solution:
    def findUnsortedSubarray(self, nums):
        if len(nums)<2:
            return 0
        sorted_nums = sorted(nums)
        first = 0
        last = 0
        for i in range(len(nums)):
            if sorted_nums[i]!=nums[i]:
                first = i
                break
        for i in range(len(nums)-1,-1,-1):
            if sorted_nums[i]!=nums[i]:
                last = i
                break
        if first-last==0:
            return 0
        else:
            return last-first+1




if __name__ == '__main__':
    inp = [1,2,3,4]
    S = Solution()
    print(S.findUnsortedSubarray(inp))