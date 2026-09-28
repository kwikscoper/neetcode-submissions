class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = prices[0]
        maxProfit = 0

        for price in prices:
            if price - lowestBuy > maxProfit:
                maxProfit = price - lowestBuy
            if price < lowestBuy:
                lowestBuy = price
            
        return maxProfit