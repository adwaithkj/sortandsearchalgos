class gossip:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        print(edges)
        for start, end, time in edges:
            print(start, end, time)

            if start in self.graphDict:
                self.graphDict[start].append(end)

            else:
                self.graphDict[start] = [(end, time)]
        print(self.graphDict)

    def findWhoKnows(self, start, end, time, path=[]):

        path = path+[start]

        if start == end:
            return path

        for node in self.graphDict[start]:
            newpath = findWhoKnows(node, end, time, path)


if __name__ == '__main__':
    edges = [
        [1, 2, 100],
        [3, 4, 200],
        [2, 4, 300]]
    g = gossip(edges)
