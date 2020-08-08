class Solution:
    def leastInterval(self, tasks, n):
        MAP = [0]*26
        for x in tasks:
            MAP[ord(x)-ord('A')]+=1
        MAP = sorted(MAP)
        time=0
        while MAP[25]>0:
            i = 0
            while(i<=n):
                if MAP[25]==0:
                    break
                if i<26 and MAP[25-i]>0:
                    MAP[25-i]-=1
                time+=1
                i+=1
            MAP = sorted(MAP)
        return time


if __name__ == '__main__':
    inp = ['A','A','B','B','Z']
    S = Solution()
    print(S.leastInterval(inp,2))