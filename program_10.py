
# Program 10: LCS and Minimum Edit Distance

# ---------- Longest Common Subsequence ----------
def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    # Create a DP table to store subsequence lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters match, increase the length
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Take the maximum of top and left cells
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # Return the length of LCS
    return dp[m][n]


# ---------- Minimum Edit Distance ----------
def min_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first column using deletions
    for i in range(m + 1):
        dp[i][0] = i

    # Initialize the first row using insertions
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # No operation is needed if characters match
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Find minimum cost among three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Replacement
                )

    # Return minimum edit distance
    return dp[m][n]


# ---------- Main Program ----------
print("PROGRAM 10")
print("LCS and Minimum Edit Distance")

# Input strings for LCS
text1 = "abcde"
text2 = "ace"

print("\nLongest Common Subsequence")
print("String 1 =", text1)
print("String 2 =", text2)
print("Length of LCS =",
      longest_common_subsequence(text1, text2))

# Input strings for edit distance
word1 = "horse"
word2 = "ros"

print("\nMinimum Edit Distance")
print("Word 1 =", word1)
print("Word 2 =", word2)
print("Minimum Operations =", min_distance(word1, word2))
