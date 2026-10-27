
# Kruskal's and Prim's MST

class Graph:
    def __init__(self, vertices):
        # Initialize the number of vertices and edge list
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        # Store an edge as (weight, source, destination)
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        # Find the root of a vertex
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        # Find roots of both vertices
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # If roots are equal, adding the edge creates a cycle
        if root_x == root_y:
            return False

        # Join the smaller-rank tree to the larger-rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    def kruskal_mst(self):
        # Initially, every vertex belongs to its own set
        parent = list(range(self.vertices))
        rank = [0] * self.vertices
        mst = []

        # Sort edges in increasing order of weight
        for weight, u, v in sorted(self.edges):
            # Add an edge only if it does not form a cycle
            if self.union(parent, rank, u, v):
                mst.append((u, v, weight))

        return mst

    def prim_mst(self):
        # Build an adjacency list for the graph
        graph = [[] for _ in range(self.vertices)]

        for weight, u, v in self.edges:
            graph[u].append((weight, v))
            graph[v].append((weight, u))

        # Start from vertex 0
        visited = [False] * self.vertices
        visited[0] = True
        mst = []

        # Select edges until the MST contains V - 1 edges
        while len(mst) < self.vertices - 1:
            minimum = None

            # Find the minimum edge connecting visited
            # and unvisited vertices
            for u in range(self.vertices):
                if visited[u]:
                    for weight, v in graph[u]:
                        if not visited[v]:
                            if minimum is None or weight < minimum[0]:
                                minimum = (weight, u, v)

            # Stop if no connecting edge exists
            if minimum is None:
                break

            weight, u, v = minimum
            visited[v] = True
            mst.append((u, v, weight))

        return mst


def main():
    # Create a graph with four vertices: 0, 1, 2, 3
    g = Graph(4)

    # Add weighted edges
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Display both minimum spanning trees
    print("Kruskal's MST:", g.kruskal_mst())
    print("Prim's MST:", g.prim_mst())


if __name__ == "__main__":
    main()
