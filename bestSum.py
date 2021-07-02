# You are given an arr and a target sum
# which you have to achieve using the
# elements from the array using least
# amount of numbers
# numbers can be repeated

class bestSum:
    shortestCombination = None                  # Class Variable

    def __init__(self, targetSum, arr):

        if targetSum == 0:
            return []

        if targetSum < 0:
            return None

        for i in arr:
            remainder = targetSum-i
            lastsum = bestSum(self, remainder, arr)
            if lastsum != None:
                combination = lastsum+[i]
                if combination < self.shortestCombination:
                    shortestCombination = combination

        return self.shortestCombination


print(bestSum(7, [5, 3, 4, 7]))
