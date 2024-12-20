def m(n):
    m = []
    print("Enter elements row by row:")
    for i in range(n):
        row = list(map(float, input(f"Enter elements for row {i + 1} separated by spaces: ").split()))
        if len(row) != n:
            print("Row length doesn't match. Please try again.")
            return m(n)
        m.append(row)
    return m


def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def row_column_sum(m):
    n = len(m)
    row_sums = [sum(row) for row in m]
    column_sums = [sum(m[i][j] for i in range(n)) for j in range(n)]
    return row_sums, column_sums

n = int(input("Enter the size of the square matrix (n x n): "))

matrix = m(n)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

transpose = transpose_matrix(matrix)
print("\nTranspose Matrix:")
for row in transpose:
    print(row)

row_sums, column_sums = row_column_sum(matrix)

sum_matrix = [row_sums, column_sums]
print("\n2 x n Matrix (Row and Column Sums):")
for row in sum_matrix:
    print(row)
