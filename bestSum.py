def bestSum(targetSum, numbers, dict1):
    if targetSum in dict1:
        return dict1[targetSum]
    if targetSum == 0:
        return []
    if targetSum <= 0:
        return None
    shortestCombination = None

    for i in numbers:
        remainderSum = targetSum-i
        combination = bestSum(remainderSum, numbers, dict1)
        if combination != None:
            combination = [i]+combination
            print(combination)
            if shortestCombination == None:
                dict1[targetSum] = combination
                shortestCombination = combination
            elif len(combination) < len(shortestCombination):
                print("Theshortestcombinatino", shortestCombination)
                dict1[targetSum] = shortestCombination
                shortestCombination = combination

    return shortestCombination


if __name__ == '__main__':
    dict1 = {}
    print("the returned value is", bestSum(100, [25, 3, 4, 2, 1], dict1))
    # print(dict1)
    dict1 = {}

# targeSUM=m n=array length
