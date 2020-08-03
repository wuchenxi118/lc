# import sys
# money = int(sys.stdin.readline())
# print(money)
# ob_num = int(sys.stdin.readline())
# print(ob_num)
# obj_list = []
# for line in sys.stdin:
#     a = line.split()
#     a = list(map(int,a))
#     obj_list.append(a)
#
# print(obj_list)
money = 100
obj_list = [
[77,92],
[22,22],
[29,36],
[50,46],
[99,90]
]
class Solution:
    def __init__(self):
        self.max_sum=0
    def solve(self,candidates,money):
        size = len(candidates)
        if size==0:
            return 0
        self.dfs(candidates,0,size,0,money)

        return self.max_sum

    def dfs(self,candidates,begin,size,n_sum,money):
        if money<=0:
            return

        for index in range(begin,size):
            money_residue = money - candidates[index][0]
            if money_residue<0:
                break
            n_sum+=candidates[index][1]
            if n_sum>self.max_sum:
                self.max_sum = n_sum
            self.dfs(candidates,begin,size,n_sum,money_residue)
            n_sum-=candidates[index][1]

S = Solution()
print(S.solve(obj_list,money))

