''' Problem : Best Time To Buy & Sell Stock With Transaction '''

#CODE :

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2: 
            return 0
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            dp[i] = dp[i-1]
            for j in range(i):
                tmp = prices[i] - prices[j] - fee
                tmp += dp[j-1] if j > 1 else 0
                dp[i] = max(dp[i], tmp)
        return dp[n-1]
        
