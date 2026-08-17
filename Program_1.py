def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def myPow(x, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / myPow(x, -n)

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# Input
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

x = float(input("Enter base: "))
n = int(input("Enter exponent: "))

# Output
print("Index:", search(nums, target))
print("Power:", myPow(x, n))