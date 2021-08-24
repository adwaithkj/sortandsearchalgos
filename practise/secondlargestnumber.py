l = [2, 1, 5, 7, 3, 3, 4, 6, 5, 2]
max = 0
secondmax = 0
for i in range(len(l)):
    if l[i] > max:
        secondmax = max
        max = l[i]
        print(max, secondmax)
    if l[i] < max and l[i] > secondmax:
        secondmax = l[i]

print(max, secondmax)
