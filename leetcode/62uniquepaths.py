# we have a grid, what do we do

# 3x2 grid, we have 3 ways of solving

# right -> down-> down      
# down  -> right-> donw
# down => down-> right

# maximum right moves=1
# maximum down moves =2

# total steps= sum of this =3

# you have to select 

# while right is remaining or ri


# right=1
# down =2

# right can exist in one of 3 places

# left can exist in 2 of 3 places

# in case of 7x3

# right=2
# down=6

# we have 8 moves
# answer is 8c(minimum of right and down-1)


from functools import reduce
import operator as op

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def ncr(n, r):
            r = min(r, n-r)
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer // denom  # or / in Python 2
        moves=m+n-2
        mini=min([m,n])
        s=0
        print(moves)
        # for i in range(1,mini):
        #     print(ncr(moves,i),moves,i)
        #     s+=ncr(moves,i)

        return ncr(moves,mini-1)
        # return s


