
class Solution:
    def __init__(self):
        self.array =[]
    def reletive_7(self , digit ):
        ans=0
        self.array = self.permute(digit)
        for i in self.array:
            int_i  = self.conv2(i)
            if int_i%7==0:
                ans+=1
        return ans

    def conv2(self,num_list):

        return sum(d*10**i for i,d in enumerate(num_list[::-1]))

    def convert_list2int(self,num_list):
        s = map(str,num_list)
        s = ''.join(s)
        s  = int(s)
        return s



    def permute(self,nums):
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
    S = Solution()
    inp = [1,1,2]
    print(S.reletive_7(inp))
