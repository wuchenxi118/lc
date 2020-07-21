class Solution:
    # def dailyTemperatures(self, T):#超时不通过的垃圾
    #     res = [0] * len(T)
    #     for i in range(len(T)):
    #         if T[i]<100:
    #             for sub_indx in range(i,len(T)):
    #                 if T[sub_indx]>T[i]:
    #                     res[i]=sub_indx-i
    #                     break
    #
    #     return res

    # def dailyTemperatures(self, T):
    #     length = len(T)
    #     ans = [0] * length
    #     next = [float('inf')] * 101
    #     for i in range(length-1,-1,-1):
    #         warmerIndex = float('inf')
    #         for t in range(T[i]+1,101):
    #             if(next[t]<warmerIndex):
    #                 warmerIndex =next[t]
    #
    #         if warmerIndex<float('inf'):
    #             ans[i] = warmerIndex - i
    #
    #         next[T[i]] = i
    #
    #     return ans

    # def dailyTemperatures(self, T):
    #     ans = [0]*len(T)
    #     stack = []
    #     for i in range(len(T)):
    #         print(stack)
    #         if len(stack)==0:
    #             stack.append([i,T[i]])
    #
    #         elif stack and T[i]>stack[-1][-1]:
    #             while stack and T[i]>stack[-1][-1]:
    #                 pop_element = stack.pop()
    #                 ans[pop_element[0]] = i - pop_element[0]
    #             stack.append([i,T[i]])
    #
    #         else:
    #             stack.append([i,T[i]])
    #
    #     print(ans)

    def dailyTemperatures(self, T):
        ans = [0]*len(T)
        stack = []
        for i in range(len(T)):
            while len(stack)!=0 and T[i]>T[stack[-1]]:
                t = stack.pop()
                ans[t] = i - t

            stack.append(i)

        return ans














if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    S =Solution()
    res = S.dailyTemperatures(temperatures)
    print(res)


