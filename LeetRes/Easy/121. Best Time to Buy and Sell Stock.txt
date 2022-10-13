class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, tmp, greatest = 0, 0, 0, 0
        j = i + 1
        while j < len(prices):
            if prices[i] < prices[j]:
                tmp = -prices[i] + prices[j]
                greatest = max(greatest, tmp)
            else:
                i = j
            j += 1
        return greatest