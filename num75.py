class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        count1 = 0
        count2 = 0
        for i in nums:
            if i==0:
                count0+=1
            if i==1:
                count1+=1
            if i==2:
                count2+=1
        nums[0:count0]=[0 for _ in range(count0)]
        nums[count0:count0+count1] = [1 for _ in range(count1)]
        nums[count0+count1:count0+count1+count2] = [2 for _ in range(count2)]

        print(nums)

    def sortColors2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0_rb = 0
        p2_lb = len(nums)-1
        cur = 0
        while cur<=p2_lb:
            if nums[cur]==0:
                nums[cur],nums[p0_rb] = nums[p0_rb],nums[cur]
                p0_rb+=1
                cur+=1
            if nums[cur]==2:
                nums[cur], nums[p2_lb] = nums[p2_lb], nums[cur]
                p2_lb-=1
            if nums[cur]==1:
                cur+=1

        print(nums)

if __name__ == '__main__':
    a = [2,0,2,1,1,0]
    S = Solution()
    S.sortColors2(a)