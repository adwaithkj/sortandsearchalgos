# You are given an arr and a target sum
# which you have to achieve using the
# elements from the array using least
# amount of numbers
# numbers can be repeated

class bestSumClass:
    def __init__(self, targetSum, arr):
        shortestCombination = None
        targetSum = self.targetSum
        arr = targetSum.arr              # Class Variable

    def bestSum(self):
        if self.targetSum == 0:
            return []

        if self.targetSum < 0:
            return None

        for i in self.arr:
            remainder = self.targetSum-i
            lastsum = bestSum(self, remainder, self.arr)
            if lastsum != None:
                combination = lastsum+[i]
                if combination < self.shortestCombination:
                    shortestCombination = combination

        return self.shortestCombination


print(bestSumClass(7, [5, 3, 4, 7]))
