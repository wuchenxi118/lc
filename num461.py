class Solution:
    def hammingDistance(self, x, y):
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        diff_len = len(x_bin)-len(y_bin)

        if diff_len>0:
            y_bin = '0'*abs(diff_len) + y_bin
        else:
            x_bin = '0'*abs(diff_len) + x_bin

        res = 0

        for i in range(len(x_bin)):
            if x_bin[i]!=y_bin[i]:
                res+=1

        return res





if __name__ == '__main__':

    x = 1
    y = 4

    S = Solution()
    print(S.hammingDistance(x,y))