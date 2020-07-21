class Solution:
    def findDuplicate(self, nums):
        len_nums = len(nums)
        left = 0
        right = len_nums - 1

        while(left<right):
            mid = left + (right-left)//2
            cnt = 0
            for x in nums:
                if x<=mid:
                    cnt+=1

            if cnt>mid:
                right = mid
            else:
                left = mid + 1

        return left

if __name__ == '__main__':
    a = [1,3,4,2,2]
    S = Solution()
    print(S.findDuplicate(a))

