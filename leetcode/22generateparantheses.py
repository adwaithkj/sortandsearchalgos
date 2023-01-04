
        
res=[]

def recursetree(n,rem=""):
    if n==0 :
        print("reached here")
        if check(rem):
            res.append(rem)
            return rem
        else:
            print("reacched else")
            return None
    
    recursetree(n-1,rem+"()")
    recursetree(n-1,rem+"((")
    recursetree(n-1,rem+")(")
    recursetree(n-1,rem+"))")

def check(rem):
    
    stack=0
    for i in rem:
        if i=="(":
            stack+=1

        if i==")" :
            if stack==0:
                return False
            else:    
                stack-=1

    if stack==0:
        return True

recursetree(1)
print(res)

    