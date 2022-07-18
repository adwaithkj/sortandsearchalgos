class Solution:
    def isBipartite(self, graph) -> bool:

        # let us create an adjacency list

        # for i in graph:
        #     if i!=[]:
        #         graph.remove(i)

        index = [i for i in range(len(graph))]
        flags = [None for i in range(len(graph))]

        self.visited = []

        def recursetree(li, index):
            print(flags, "each recursion", self.visited)

            if index not in self.visited:
                self.visited.append(index)

            if len(self.visited) == len(graph):
                print(flags, True)
                return True

            if flags[index] == None:
                flags[index] = 1

            for i in li:

                if flags[i] == None:
                    if flags[index] == 1:
                        flags[i] = 0
                    elif flags[index] == 0:
                        flags[i] = 1

                if flags[index] == flags[i]:
                    print(flags, False, self.visited,
                          " flag of index same as flag of i")
                    return False

            for i in li:
                if i not in self.visited:
                    if recursetree(graph[i], i):
                        print(flags, True, self.visited)

                        return True
                    else:
                        print(flags, False, self.visited)

                        return False

            return True

        return recursetree(graph[0], 0)


# class Solution(object):
#     def isBipartite(self, g):
#         n = len(g)
#         part = [-1 for _ in range(n)]
#         for i in range(n):
#             if part[i]==-1:
#                 q = deque([i])
#                 part[i] = 0
#                 while len(q)>0:
#                     for u in g[q[0]]:
#                         if part[u]==-1:
#                             part[u] = 1 - part[q[0]]
#                             q.append(u)
#                         else:
#                             if part[u] == part[q[0]]: return False
#                     q.popleft()
#         return True
