from typing import List, Tuple


def findKthLargest(nums: List[int], k: int) -> int:
    # Sort the array in descending order
    nums = sorted(nums, reverse=True)

    # k-th largest element
    return nums[k - 1]


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    # Find minimum and maximum elements
    minimum = min(nums)
    maximum = max(nums)

    return minimum, maximum


# Example

nums = list(map(int, input("Enter array elements: ").split()))

k = int(input("Enter k: "))

print("Array:", nums)
print(f"{k}th Largest Element:", findKthLargest(nums, k))

minimum, maximum = findMinMax(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)