class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_on = prices[0]
        n = len(prices)
        res = 0

        for i in range(1,n):
            if prices[i] < buy_on:
                buy_on = prices[i]
            else:
                if prices[i] - buy_on > res:
                    res = prices[i] - buy_on

        return res


            
            

            
        