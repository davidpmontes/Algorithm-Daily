class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        minPrice = float("inf")
        
        for i in range(0, len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minPrice)
            
        return maxProfit
