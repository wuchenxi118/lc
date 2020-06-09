class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        temp = []
        res = []
        dic={}
        for i in range(len(strs)):
            letter_sorted = ''.join(sorted(list(strs[i])))
            temp.append(letter_sorted)

        for j in range(len(temp)):
            if temp[j] not in dic:
                dic[temp[j]] = [strs[j]]
            else:
                dic[temp[j]].append(strs[j])

        for i in dic:
            res.append(dic[i])

        return res













if __name__ == '__main__':
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    S = Solution()
    res = S.groupAnagrams(inp)
    print(res)