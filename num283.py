class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        len_nums = len(nums)
        indx = 0
        res = []
        zero = []
        while(indx<len_nums):
            if nums[indx]!=0:
                res.append(nums[indx])
                indx+=1
            else:
                zero.append(0)
                indx += 1

        for idx,num in enumerate(res+zero):
            nums[idx] = num

        return nums








if __name__ == '__main__':
    a = [0,1,0,3,12]
    S = Solution()
    print(S.moveZeroes(a))
