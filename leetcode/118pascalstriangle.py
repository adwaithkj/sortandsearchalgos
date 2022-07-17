class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        self.result = []

        def recursetree(n):

            if n == 1:
                self.result += [[1]]
                return [1]
            if n == 2:
                self.result += [[1]]+[[1, 1]]
                return [1, 1]

            last = recursetree(n-1)
            print(last)
            res = [0 for i in range(n)]

            res[0] = 1
            res[-1] = 1

            for i in range(1, n-1):
                res[i] = last[i-1]+last[i]
            self.result += [res]

            return res

        recursetree(numRows)
        print(self.result)

        return self.result
