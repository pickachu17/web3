class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maximumProfit, minStockVal = 0, float('inf')
        i = 0
        while i < n:
            minStockVal = min(minStockVal, prices[i])
            if prices[i] >= minStockVal:
                maximumProfit = max(maximumProfit, prices[i] - minStockVal)
            i += 1
        return maximumProfit