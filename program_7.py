
# Dijkstra's and Bellman-Ford Algorithms

class ShortestPath:
    def __init__(self, vertices):
        # Initialize the number of vertices and edge list
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        # Store a directed edge
        self.edges.append((u, v, weight))

    def dijkstra(self, src):
        # Create an adjacency list
        graph = [[] for _ in range(self.vertices)]

        for u, v, weight in self.edges:
            # Dijkstra does not support negative weights
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            graph[u].append((v, weight))

        # Initialize distances to infinity
        dist = [float('inf')] * self.vertices
        visited = [False] * self.vertices
        dist[src] = 0

        # Process each vertex
        for _ in range(self.vertices):
            u = -1

            # Find the unvisited vertex with minimum distance
            for i in range(self.vertices):
                if not visited[i] and (
                    u == -1 or dist[i] < dist[u]
                ):
                    u = i

            # Stop if remaining vertices are unreachable
            if u == -1 or dist[u] == float('inf'):
                break

            visited[u] = True

            # Update distances of neighboring vertices
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        return dist

    def bellman_ford(self, src):
        # Initialize all distances to infinity
        dist = [float('inf')] * self.vertices
        dist[src] = 0

        # Relax all edges V - 1 times
        for _ in range(self.vertices - 1):
            changed = False

            for u, v, weight in self.edges:
                if dist[u] != float('inf'):
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        changed = True

            # Stop early if no distance changes
            if not changed:
                break

        # Check for a reachable negative-weight cycle
        for u, v, weight in self.edges:
            if dist[u] != float('inf'):
                if dist[u] + weight < dist[v]:
                    return "Negative-weight cycle detected"

        return dist


def main():
    # Create a graph with five vertices
    g = ShortestPath(5)

    # Add directed edges with weights
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)

    # Calculate shortest distances from source vertex 0
    print("Dijkstra distances:", g.dijkstra(0))
    print("Bellman-Ford distances:", g.bellman_ford(0))


if __name__ == "__main__":
    main()
