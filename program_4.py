from typing import List

def add_matrix(A, B):
    n = len(A)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result


def subtract_matrix(A, B):
    n = len(A)
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[i][j] - B[i][j])
        result.append(row)

    return result


def strassen_multiply(A: List[List[int]],
                      B: List[List[int]]) -> List[List[int]]:

    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide A into four parts
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide B into four parts
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Seven Strassen products

    M1 = strassen_multiply(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2 = strassen_multiply(
        add_matrix(A21, A22),
        B11
    )

    M3 = strassen_multiply(
        A11,
        subtract_matrix(B12, B22)
    )

    M4 = strassen_multiply(
        A22,
        subtract_matrix(B21, B11)
    )

    M5 = strassen_multiply(
        add_matrix(A11, A12),
        B22
    )

    M6 = strassen_multiply(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7 = strassen_multiply(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    # Calculate result submatrices

    C11 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M4),
            M5
        ),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M3),
            M2
        ),
        M6
    )

    # Combine C11, C12, C21, C22
    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


# Main program
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = strassen_multiply(A, B)

print("Product Matrix:")

for row in result:
    print(row)
