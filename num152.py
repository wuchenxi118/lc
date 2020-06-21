class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = -float('inf')
        max_tmp = 1
        min_tmp = 1
        for i in nums:
            if i<0:
                tmp = max_tmp
                max_tmp = min_tmp
                min_tmp = tmp

            max_tmp = max(i,max_tmp*i)
            min_tmp = min(i,min_tmp*i)

            max_num = max(max_num,max_tmp)

        return max_num