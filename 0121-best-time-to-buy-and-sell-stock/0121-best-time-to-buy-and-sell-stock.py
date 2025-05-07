class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=prices[0],prices[0]
        res = 0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
                sell=prices[i]
            if prices[i]>sell:
                sell=prices[i]
            res = max(res,sell-buy)
        return res
        