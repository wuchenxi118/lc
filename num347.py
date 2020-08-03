class Solution:
    def topKFrequent(self, nums, k):
        res_list = []
        res = []
        nums_set = set(nums)
        for num in nums_set:
            res_list.append([num,nums.count(num)])

        res_list = sorted(res_list,key=lambda x:x[-1],reverse=True)
        for i in range(k):
            if i<len(res_list):
                res.append(res_list[i][0])


        return res



if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 10
    S =Solution()
    print(S.topKFrequent(nums,k))