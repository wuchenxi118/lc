from collections import Counter
class Solution:
    # def majorityElement(self, nums):
    #     L = len(nums)
    #     n = int(L/2)
    #     result = Counter(nums)
    #     print(result)
    #
    #     for i in result:
    #         if result[i]>n:
    #             return i

    # def majorityElement(self, nums):
    #     L = len(nums)
    #     n = int(L/2)
    #     result = {}
    #     for key in nums:
    #         result[key] = result.get(key,0) + 1
    #
    #     for i in result:
    #         if result[i]>n:
    #             return i
    def majorityElement(self, nums):
        L = len(nums)
        n = int(L/2)
        nums.sort()

        return nums[n]




if __name__ == '__main__':
    nums = [1,1,1,1,2,2,2,3,3,3,1,1,1,1]

    S = Solution()

    print(S.majorityElement(nums))

