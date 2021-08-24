s = "adwaith"
stack = []
for i in s:
    stack += [i]
rev = ""
while stack != []:
    rev += stack.pop()
print(rev)
