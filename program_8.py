
# Huffman Coding

import heapq
from itertools import count

class Node:
    def __init__(self, char, freq, left=None, right=None):
        # Store character, frequency and child nodes
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

class HuffmanCoder:
    def build_tree(self, frequencies):
        # Return None if no characters are provided
        if not frequencies:
            return None

        heap = []
        unique_id = count()

        # Create a leaf node for each character
        for char, freq in frequencies.items():
            if freq <= 0:
                raise ValueError("Frequencies must be positive")

            # Use a unique ID to handle equal frequencies
            heapq.heappush(
                heap, (freq, next(unique_id), Node(char, freq))
            )

        # Combine the two nodes with lowest frequencies
        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            # Create a parent node for the two nodes
            merged = Node(None, freq1 + freq2, left, right)

            heapq.heappush(
                heap, (merged.freq, next(unique_id), merged)
            )

        # The remaining node is the root of the Huffman tree
        return heap[0][2]

    def generate_codes(self, root):
        # Dictionary to store character-to-code mappings
        codes = {}

        def traverse(node, code):
            # Stop if the node is empty
            if node is None:
                return

            # Save the code when a leaf node is reached
            if node.char is not None:
                codes[node.char] = code or "0"
                return

            # Left edge represents 0; right edge represents 1
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(root, "")
        return codes


def main():
    # Character frequencies
    frequencies = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    # Build the Huffman tree and generate codes
    coder = HuffmanCoder()
    root = coder.build_tree(frequencies)
    codes = coder.generate_codes(root)

    # Display the generated binary codes
    print("Huffman Codes:")
    for char in sorted(codes):
        print(char, ":", codes[char])


if __name__ == "__main__":
    main()
