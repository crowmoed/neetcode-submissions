class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bday,sday = 0,0
        profit = 0
        for index,pr in enumerate(prices):
            if (prices[sday]<pr):
                sday = index
            if (prices[bday]>pr):
                bday = index
            profit = max(profit, pr - prices[bday])
        return profit