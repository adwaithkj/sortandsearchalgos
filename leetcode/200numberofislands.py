class Solution:
    def numIslands(self, grid) -> int:

        counter = 0

        y = len(grid)
        x = len(grid[0])

        def callBFS(i, j, grid):

            if grid[i][j] == '1':
                grid[i][j] = '0'
                if i+1 < y:
                    callBFS(i+1, j, grid)
                if j+1 < x:
                    callBFS(i, j+1, grid)
                if i > 0:
                    callBFS(i-1, j, grid)
                if j > 0:
                    callBFS(i, j-1, grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1

                    callBFS(i, j, grid)

        return counter
