class Solution:
    def __init__(self):
        self.dic_ls = {}
        self.dic_t = {}
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        for i in t:
            if i not in self.dic_t:
                self.dic_t[i]=1
            else:
                self.dic_t[i]+=1
        print(self.dic_t)
        print()
        left = 0
        right = 0
        min_len = len(s)+1
        min_window=[0,0]
        while(right<len(s)):
            # print(s[min_window[0]:min_window[1]])
            # print(left,right)
            while(not self.compare() and right<len(s)):
                right+=1
                if s[right-1] not in self.dic_ls:
                    self.dic_ls[s[right-1]]=1
                else:
                    self.dic_ls[s[right-1]]+=1
            if right-left < min_len:
                min_len = right-left
                min_window=[left,right]

            print('ori',self.dic_ls,left,right)
            while(self.compare()):
                # print(self.dic_ls)
                left+=1
                print(left)
                print(s[left-1])
                self.dic_ls[s[left-1]]-=1
                # print(self.dic_ls)
            # left-=1
            if right-left-1 < min_len:
                min_len = right-left
                min_window=[left-1,right]
        if min_window[0]==-1:
            return ""
        else:
            return s[min_window[0]:min_window[1]]


    # def minWindow(self, s: str, t: str) -> str:
    #     if len(t)>len(s):
    #         return ""
    #     for i in t:
    #         if i not in self.dic_t:
    #             self.dic_t[i]=0
    #         else:
    #             self.dic_t[i]+=1
    #     l = 0
    #     r = -1
    #     mlen = len(s)+1
    #     ansL = -1
    #     ansR = -1
    #     while r < len(s):
    #         r+=1
    #         if s[r] in self.dic_t:
    #             if s[r] not in self.dic_ls:
    #                 self.dic_ls[s[r]]=0
    #             else:
    #                 self.dic_ls[s[r]]+=1
    #         while(self.compare() and l<=r):
    #             if(r-l+1<mlen):
    #                 mlen = r-l+1
    #                 ansL = l
    #             if(s[l] in self.dic_t):
    #                 self.dic_ls[s[l]]-=1
    #             l+=1







    def compare(self):
        for i in self.dic_t:
            if (i in self.dic_ls) and (self.dic_ls[i]>=self.dic_t[i]):
                pass
            else:
                return False
        return True





if __name__ == '__main__':
    s = "a"
    t = "b"
    S=Solution()
    print(S.minWindow(s,t))
