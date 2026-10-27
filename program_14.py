# Program 14: N-Queens Problem

def solveNQueens(n):
    result = []

    # Create an empty chessboard
    board = [["."] * n for _ in range(n)]

    def solve(row):
        # If all queens are placed, save the board
        if row == n:
            result.append(["".join(line) for line in board])
            return

        # Try placing a queen in each column
        for col in range(n):

            # Check the same column
            safe = True

            for r in range(row):
                if board[r][col] == "Q":
                    safe = False
                    break

            # Check the upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    safe = False
                    break
                r -= 1
                c -= 1

            # Check the upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    safe = False
                    break
                r -= 1
                c += 1

            # Place a queen if the position is safe
            if safe:
                board[row][col] = "Q"
                solve(row + 1)

                # Remove the queen during backtracking
                board[row][col] = "."

    solve(0)
    return result


# Main program
n = int(input("Enter the value of N: "))

solutions = solveNQueens(n)

print("Total Solutions:", len(solutions))

for solution in solutions:
    for row in solution:
        print(row)
    print()