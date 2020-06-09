class Solution:
    def canJump(self, nums):
        if not nums:
            return False

        max_dir = nums[0]
        now_dir = 0
        while (now_dir<max_dir):
            now_dir+=1
            max_dir = max(nums[now_dir]+now_dir,max_dir)
            if max_dir == len(nums)-1:
                return True

        return False


if __name__ == '__main__':
    inp =  [2,3,1,1,4]
    S = Solution()
    print(S.canJump(inp))