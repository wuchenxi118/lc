import time
class Solution:
    def subsets(self, nums):   #递归
        start = time.time()
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]
        print(time.time()-start)
        return output

    # def subsets(self, nums):
    #     start=time.time()
    #     def backtrack(first = 0,curr = []):
    #         if len(curr) == k:
    #             output.append(curr.copy())
    #         for i in range(first,n):
    #             curr.append(nums[i])
    #             backtrack(i+1,curr)
    #             curr.pop()
    #
    #     output=[]
    #     n = len(nums)
    #     for k in range(n+1):
    #         backtrack()
    #     print(time.time()-start)
    #     return output

if __name__ == '__main__':
    nums = [1,2,3]
    S = Solution()
    print(S.subsets(nums))
