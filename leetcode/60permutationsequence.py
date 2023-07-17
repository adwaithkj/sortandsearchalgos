# so 123

# 1 will be at units place for 2! times
# n-1!


# so k=3

# no of times k is divisible by n-1 


# for i in range(n):
	

# 123

# k=3

# 123
# 132
# 213
# 231
# 312
# 321

# k=3
# we have to consider 3-1=2
# 2 is divisible by (n-1)! 1 time
# so initial digit is index 1 of the array [1,2,3]

# now let us remove index 1->[1,2,3] ==> [1,3]

# then remainder is 0 
# now 0 is divisible by 1! 0 time

# now removing 0th index we have  [1,3]-->[3]

# remainder is 0 again.


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        li=[]
        di={}
        def factorial(n):
            if n==1 or n==0:
                return 1
            if n in di:
                return di[n]
            di[n]= n*factorial(n-1)
            return di[n]

        newn=factorial(n)

        for i in range(n):
            li.append(i+1)
        
        num=k-1
        res=[]
        for i in range(n):
            div=num//factorial(n-i-1)
            res=res+[li[div]]
            del li[div]
            num=num%factorial(n-i-1)
        
        ans=list(map(str,res))
        return "".join(ans)



