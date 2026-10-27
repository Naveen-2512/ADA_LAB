# Longest Increasing Subsequence

def lengthOfLIS(nums):
    # Handle an empty list
    if not nums:
        return 0

    # Store the length of the increasing subsequence
    dp = [1] * len(nums)

    # Check each element
    for i in range(len(nums)):
        for j in range(i):
            # Update length if the current element is greater
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum length
    return max(dp)


# Main program
nums = list(map(int, input("Enter integers separated by spaces: ").split()))

print("Length of Longest Increasing Subsequence:", lengthOfLIS(nums))