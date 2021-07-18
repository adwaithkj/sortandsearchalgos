# there are two ways of representing a graph
# we can use an adjacency list
# the other way is to use an adjacency matrix
# its easier to represent weighted graphs using an adjacency matrix
# we can represent a directed graph using both structures
# so which is better
# dense graph is where number of Edges is Vertex squared
# sparese garph is where edges is equal to vertices
# an adjacent list is faster and uses less space for sparse garphs
# a con is that is it slower for dense graphs
# Adjacency matrix is faster for dense graphs
# simpler for weighted edges.
# con is that it uses more space

# implemetation of an undirected graph using adjacency lists
# graphs and trees are recursive data strctures

class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary is ", self.graph_dict, "\n\n\n")

    def get_paths(self, start, end, path=[]):
        path = path+[start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path+[start]

        if start == end:
            return path
        if start not in self.graph_dict:
            return []
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_shortest_path(node, end, path)
                if shortest_path == None:
                    shortest_path = new_path

                if len(new_path) < len(shortest_path):
                    shortest_path = new_path
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print("These are all the possible paths between", start, "and", end, "\n", route_graph.get_paths(
        start, end))
    print("\nThe shortes path between", start, "and", end,
          route_graph.get_shortest_path(start, end))

#       ┌───────► paris──────────────┐
#       │          │                 │
#       │          │                 │
# mumbai           │                 ▼
#      │           │            new york──────────────► toronto
#      │           │                 ◄┐
#      │           │                  │
#      │           │                  │
#      │           ▼                  │
#      └────────►dubai ───────────────┘

# for reference
