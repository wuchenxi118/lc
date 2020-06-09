class Solution:
    def permute(self, nums):
        if len(nums)==0:
            return []
        res = []
        size = len(nums)
        used = [False for i in range(size)]
        self._dfs(used,[],res,size,nums)
        return res



    def _dfs(self,used,path,res,size,nums):
        if len(path)==size:
            res.append(path.copy())
            return
        for i in range(size):
            if used[i] == False:
                used[i] = True
                self._dfs(used=used,path=path+[nums[i]],res=res,size=size,nums=nums)
                used[i] = False











if __name__ == '__main__':

    a = [1,2,3]
    S = Solution()
    print(S.permute(a))
