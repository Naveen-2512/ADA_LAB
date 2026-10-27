# Program 15: Graph Coloring and Hamiltonian Cycle

class GraphBacktracker:

    def __init__(self, graph):
        # Store the adjacency matrix
        self.graph = graph
        self.n = len(graph)

    # Graph Coloring Problem
    def graph_coloring(self, m):
        # Initially, no vertex has a color
        colors = [0] * self.n

        def is_safe(vertex, color):
            # Check colors of adjacent vertices
            for i in range(self.n):
                if self.graph[vertex][i] == 1:
                    if colors[i] == color:
                        return False
            return True

        def solve(vertex):
            # All vertices are colored
            if vertex == self.n:
                return True

            # Try each available color
            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color

                    if solve(vertex + 1):
                        return True

                    # Backtrack
                    colors[vertex] = 0

            return False

        if solve(0):
            return colors

        return []

    # Hamiltonian Cycle Problem
    def hamiltonian_cycle(self):
        if self.n == 0:
            return []

        path = [0]

        def is_safe(vertex):
            # Check connection with the previous vertex
            if self.graph[path[-1]][vertex] == 0:
                return False

            # A vertex cannot be repeated
            if vertex in path:
                return False

            return True

        def solve():
            # Check whether all vertices are included
            if len(path) == self.n:
                # Check connection back to the starting vertex
                return self.graph[path[-1]][path[0]] == 1

            # Try the remaining vertices
            for vertex in range(1, self.n):
                if is_safe(vertex):
                    path.append(vertex)

                    if solve():
                        return True

                    # Backtrack
                    path.pop()

            return False

        if solve():
            return path + [path[0]]

        return []


# Main program
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

obj = GraphBacktracker(graph)

m = int(input("Enter the number of colors: "))

print("Vertex Colors:", obj.graph_coloring(m))
print("Hamiltonian Cycle:", obj.hamiltonian_cycle())