from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size==0:
            return []
        used = [False]*size
        candidates.sort()
        res=[]
        self._dfs(candidates,target,0,size,[],res,used)
        res = list(map(tuple, res))
        res = list(map(list,set(res)))
        return res



    def _dfs(self,candidates,target,begin,size,path,res,used):
        if target==0:
            res.append(path.copy())
            return


        for i in range(begin,size):
            if used[i]==True:
                continue
            # if i > begin and candidates[i - 1] == candidates[i]:
            #     continue

            residue = target-candidates[i]
            if residue<0:
                break
            path.append(candidates[i])
            used[i] = True
            self._dfs(candidates,residue,i+1,size,path,res,used)
            used[i] = False
            path.pop()


def hash_map(inp):

    inp = list(map(tuple,inp))
    inp = set(inp)



if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    S = Solution()
    inp = S.combinationSum2(candidates,target)
    print(inp)
    print(hash_map(inp))


