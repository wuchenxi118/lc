class Solution:
    # def singleNumber(self, nums):
    #     num_set = set(nums)
    #     set_sum = sum(num_set)*2
    #     ori_sum = sum(nums)
    #     return int(set_sum-ori_sum)

    def singleNumber(self, nums):
        single =0
        for i in nums:
            single ^= i
        return single
if __name__ == '__main__':
    a = [4,1,1,2,2]
    S = Solution()
    print(S.singleNumber(a))