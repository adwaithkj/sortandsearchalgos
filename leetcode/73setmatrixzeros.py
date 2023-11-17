class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        for i in range(len(matrix)):
            flag=0
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    flag=1
                    
                elif flag==1:
                    matrix[i][j]=-69
        
        for i in range(len(matrix)):
            flag=0
            for j in range(len(matrix[0])):
                if matrix[i][-j-1]==0:
                    flag=1
                    
                elif flag==1:
                    matrix[i][-j-1]=-69

        for i in range(len(matrix[0])):
            flag=0
            for j in range(len(matrix)):
                
                if matrix[j][i]==0:
                    flag=1
                    
                elif flag==1 :
                    matrix[j][i]=-69

        for i in range(len(matrix[0])):
            flag=0
            for j in range(len(matrix)):
                if matrix[-j-1][i]==0:
                    flag=1
                    
                elif flag==1:
                    matrix[-j-1][i]=-69

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-69:
                    matrix[i][j]=0
        return matrix

