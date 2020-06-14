class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n==0:
            return 0
        minprice=float('inf')
        dp = [0]*n
        for i in range(1,len(prices)):
            minprice = min(minprice,prices[i-1])
            dp[i] = max(dp[i-1],prices[i]-minprice)
        return dp[-1]

    def maxProfit2(self, prices):
        n = len(prices)
        if n==0:
            return 0
        minprice=float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            minprice = min(minprice,prices[i])
            maxprofit = max(maxprofit,prices[i]-minprice)



        return maxprofit

if __name__ == '__main__':
    prices= [7,1,5,3,6,4]
    S =Solution()
    print(S.maxProfit2(prices))

