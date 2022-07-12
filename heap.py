# We are going to implemetnt heapq in this program


path = [1, 2, 3, 4]


def changepath(path):
    path.append(5)

    return None


changepath(path+[6])


print(path)
