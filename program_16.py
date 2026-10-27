# Program 16: KMP String Matching

def strStr(haystack, needle):
    # An empty pattern matches at index 0
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    # Create the LPS (Longest Prefix Suffix) array
    lps = [0] * m
    length = 0
    i = 1

    # Build the LPS array
    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search for the pattern in the text
    i = 0
    j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == m:
            # Return the first matching index
            return i - j

        elif i < n and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    # Pattern not found
    return -1


# Randomizer Class for Stream Sampling

import random


class Randomizer:

    def __init__(self):
        # Store the number of elements processed
        self.count = 0

        # Store the selected element
        self.selected = None

    def add(self, item):
        # Increase the number of processed elements
        self.count += 1

        # Select the first element automatically
        if self.count == 1:
            self.selected = item

        else:
            # Replace the selected element with probability 1/count
            if random.randint(1, self.count) == 1:
                self.selected = item

    def getRandom(self):
        # Return the randomly selected element
        return self.selected


# Main program: KMP String Matching
haystack = input("Enter the text: ")
needle = input("Enter the pattern: ")

print("Pattern Index:", strStr(haystack, needle))

# Main program: Random Sampling
data = input("Enter stream elements separated by spaces: ").split()

randomizer = Randomizer()

# Process every element in the stream
for item in data:
    randomizer.add(item)

print("Randomly Selected Element:", randomizer.getRandom())