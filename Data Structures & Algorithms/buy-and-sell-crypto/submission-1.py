class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        maxProfit=0

        for price in prices:
            if price<minPrice:
                minPrice=price
            else:
                Profit=price-minPrice
                maxProfit=max(Profit,maxProfit)
        return maxProfit