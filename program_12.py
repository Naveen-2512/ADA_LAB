# Program 12: Floyd-Warshall Algorithm

def floyd_warshall(graph):
    # Copy the graph to create the distance matrix
    dist = [row[:] for row in graph]
    n = len(graph)

    # Consider every vertex as an intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update distance if a shorter path exists
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist


# Optimal Binary Search Tree

def optimal_bst(keys, freq):
    n = len(keys)

    # Empty input has zero cost
    if n == 0:
        return 0

    # Create a cost table
    cost = [[0] * n for _ in range(n)]

    # Cost of a single key
    for i in range(n):
        cost[i][i] = freq[i]

    # Consider subtrees of increasing sizes
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")

            # Calculate the sum of frequencies
            total = sum(freq[i:j + 1])

            # Try every key as the root
            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                current = left + right + total
                cost[i][j] = min(cost[i][j], current)

    return cost[0][n - 1]


# Main program: Floyd-Warshall
graph = [
    [0, 5, 999, 10],
    [999, 0, 3, 999],
    [999, 999, 0, 1],
    [999, 999, 999, 0]
]

print("Shortest Distance Matrix:")
for row in floyd_warshall(graph):
    print(row)

# Main program: Optimal BST
keys = [10, 20, 30]
freq = [34, 8, 50]

print("Minimum Cost of Optimal BST:", optimal_bst(keys, freq))