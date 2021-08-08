class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        retarr = []
        intervals.sort(key=lambda x: x[0])

        flag = 0
        for i, j in intervals:
            if flag == 0:
                flag = 1
                stack.append(intervals[0])
            elif stack[-1][1] >= i and stack[-1][1] <= j:
                stack[-1][1] = j
            elif stack[-1][1] >= i and stack[-1][1] > j:
                continue
            else:
                stack.append([i, j])

        return stack
