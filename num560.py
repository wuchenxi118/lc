from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0

        if len(nums)==1:
            if nums[0]==k:
                return 1
            else:
                return 0

        for i in range(len(nums)):
            nsum = nums[i]
            if nsum == k:
                res+=1
            for j in range(i+1,len(nums)):
                nsum+=nums[j]
                if nsum==k:
                    res+=1

        return res

if __name__ == '__main__':
    nums = [1,2,3]
    k = 3
    S = Solution()
    print(S.subarraySum(nums,k))
