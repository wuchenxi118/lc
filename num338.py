from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[]
        for i in range(num+1):
            bin_i = bin(i).replace('0b','')
            one_count = list(bin_i).count('1')
            res.append(one_count)

        return res




if __name__ == '__main__':
    num = 2
    S = Solution()
    print(S.countBits(num))
