def quick_sort(collection, low, high):
    # 快速排序
    if low >= high:
        return collection
    else:
        pivot = collection[low]    # 把第一个作为基准值
        left = low
        right = high
        while left < right:
            while left < right and collection[right] >= pivot:
                right -= 1    # 右边的哨兵左移一个
            collection[left] = collection[right]
            while left < right and collection[left] <= pivot:
                left +=1    # 左边的哨兵右移一个
            collection[right] = collection[left]
        collection[right] = pivot    # 两个哨兵相遇时则说明找到基准值的位置
        quick_sort(collection, low, left-1)    # 递归左半部分
        quick_sort(collection, left+1, high)    # 递归右半部分
        return collection


class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums = quick_sort(nums,0,len(nums)-1)
        max_num = 1
        litte_num = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                litte_num+=1
                max_num = max(max_num, litte_num)
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                litte_num=1
        return max_num

    def longestConsecutive2(self, nums):
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num+1 in num_set:
                    current_num+=1
                    current_streak+=1

                longest_streak = max(longest_streak,current_streak)
        return longest_streak





if __name__ == '__main__':
    nums = [1,2,0,1]
    S = Solution()
    print(S.longestConsecutive2(nums))