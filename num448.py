class Solution:
    # def findDisappearedNumbers(self, nums):
    #     n = len(nums)
    #     nums = sorted(nums)
    #     nums = list(set(nums)) + [0]*(n+1-len(nums))
    #     print(nums)
    #     res = []
    #     nums_index = 0
    #     for i in range(1,n+1):
    #         if nums[nums_index] == i:
    #             nums_index+=1
    #         else:
    #             res.append(i)
    #
    #
    #
    #
    #     return res

    # def findDisappearedNumbers(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #
    #     # Hash table for keeping track of the numbers in the array
    #     # Note that we can also use a set here since we are not
    #     # really concerned with the frequency of numbers.
    #     hash_table = {}
    #
    #     # Add each of the numbers to the hash table
    #     for num in nums:
    #         hash_table[num] = 1
    #
    #     # Response array that would contain the missing numbers
    #     result = []
    #
    #     # Iterate over the numbers from 1 to N and add all those
    #     # that don't appear in the hash table.
    #     for num in range(1, len(nums) + 1):
    #         if num not in hash_table:
    #             result.append(num)
    #
    #     return result
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Iterate over each of the elements in the original array
        for i in range(len(nums)):

            # Treat the value as the new index
            new_index = abs(nums[i]) - 1

            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result




if __name__ == '__main__':
    inp = [1,1]
    S = Solution()
    print(S.findDisappearedNumbers(inp))

