class Solution:
    def maxProfit(self, prices) -> int:

        lowest = prices[0]
        maxdiff = 0

        for i in prices:
            if i < lowest:
                lowest = i
            if i-lowest > maxdiff:
                maxdiff = i-lowest
        return maxdiff
