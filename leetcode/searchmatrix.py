class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[1])
        
        
        rowflag=0
        li=list(map(lambda x: x[0],matrix))

        while True:
            rowmid=li[len(li)//2]
            if len(li)==1 or rowmid==target:
                row=rowmid
                break
            elif rowmid>target:
                li=li[len(li)//2+1:]
            else:
                li=li[:len(li)//2]
