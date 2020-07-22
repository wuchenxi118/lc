class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            print(center%2)
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

    def countSubstrings_v2(self, S):
        N = len(S)
        ans = 0
        for i in range(N):
            left = i
            right = i
            while left>=0 and right<N and S[left]==S[right]:
                ans+=1
                left-=1
                right+=1

        for i in range(N):
            left = i
            right = i+1
            while left>=0 and right<N and S[left]==S[right]:
                ans+=1
                left-=1
                right+=1
        return ans


if __name__ == '__main__':
    a = 'aaa'
    S =Solution()
    print(S.countSubstrings_v2(a))
