# The question is if you are given an array of magnitude and 1 dimensional direction, find the maximum distance that can be traversed
# find the maximum distance that can be traversed by removing same amount of vectors pointing the 2 different directions


def countof(q, d):
    countl = 0
    countr = 0
    for i in q:
        if d[i] == 'R':
            countr += 1
        else:
            countl += 1
    return countl, countr


def removal(index, D, direction):
    for i in index:

        del D[i]
        del direction[i]


def distance(D, direction):

    length = 0
    for i in range(len(D)):
        if direction[i] == 'R':
            length += D[i]
        else:
            length -= D[i]

    return abs(length)


def solve(n, D, direction):
    # print("this is n "+ str(n) +"this is D "+ str(D)+ "and this is direction " +str(direction)

    R = []
    for i in direction:
        if i == 'R':
            R.append(i)

    L = []
    for i in direction:
        if i == 'L':
            L.append(i)

    largestDistance = distance(D, direction)

    for i in range(len(D)):
        q = []
        for j in range(i, len(D)):
            q.append(j)
            dirn = direction[:]
            d = D[:]

            countl, countr = countof(q, d)
            # if countl == countr:
            #     removal(q, d, dirn)

            #     print(f"{d} is d and that {dirn} is the dirn")
            #     if distance(d, dirn) > largestDistance:
            #         largestDistance = distance(d, dirn)

            removal(q, d, dirn)

            print(f"{d} is d and that {dirn} is the dirn")
            if distance(d, dirn) > largestDistance and countl == countr:

                largestDistance = distance(d, dirn)

    return largestDistance

    # Write your code here

# T = int(input())
# for _ in range(T):
# 	D = []
# 	direction = []
# 	n=int(input())
# 	for i in range(n):
# 		s=input().split(' ')
# 		D.append(int(s[0]))
# 		direction.append(s[1])
# 	out_ = solve(n, D, direction)
# 	print (out_)


n = 5
D = [1, 2, 3, 4, 5]
direction = ['R', 'L', 'R', 'R', 'L']

print(solve(n, D, direction))
