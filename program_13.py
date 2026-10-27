# Program 13: Travelling Salesman Problem

class TSPSolver:

    def solve_tsp(self, dist_matrix):
        n = len(dist_matrix)

        # Handle an empty matrix
        if n == 0:
            return 0

        # Track visited cities
        visited = [False] * n
        visited[0] = True

        # Find the minimum tour cost
        def tsp(city, count, cost):
            # Return to the starting city after visiting all cities
            if count == n:
                return cost + dist_matrix[city][0]

            minimum = float("inf")

            # Visit each unvisited city
            for next_city in range(n):
                if not visited[next_city]:
                    visited[next_city] = True

                    result = tsp(
                        next_city,
                        count + 1,
                        cost + dist_matrix[city][next_city]
                    )

                    minimum = min(minimum, result)

                    # Backtrack
                    visited[next_city] = False

            return minimum

        return tsp(0, 1, 0)


# Main program
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solver = TSPSolver()

print("Minimum Tour Cost:", solver.solve_tsp(dist_matrix))