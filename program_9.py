
# 0/1 Knapsack Using Dynamic Programming

# ---------- 2D Dynamic Programming ----------
def knapsack_2d(weights, values, capacity):
    n = len(weights)

    # Create a DP table initialized with zeros
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Process each item
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            # Check whether the item fits
            if weights[i - 1] <= w:
                # Choose maximum value by including
                # or excluding the current item
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Exclude the item if it does not fit
                dp[i][w] = dp[i - 1][w]

    # Return maximum value
    return dp[n][capacity]


# ---------- 1D Dynamic Programming ----------
def knapsack_1d(weights, values, capacity):
    # Create a one-dimensional DP array
    dp = [0] * (capacity + 1)

    # Process each item
    for i in range(len(weights)):

        # Iterate backwards to avoid selecting
        # the same item more than once
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    return dp[capacity]


# ---------- Main Program ----------
print("PROGRAM 9")
print("0/1 Knapsack Problem")

# Item weights and values
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

# Display results using both methods
print("\nUsing 2D Dynamic Programming")
print("Maximum Value =", knapsack_2d(weights, values, capacity))

print("\nUsing 1D Dynamic Programming")
print("Maximum Value =", knapsack_1d(weights, values, capacity))
