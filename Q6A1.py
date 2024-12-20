import numpy as np
import matplotlib.pyplot as plt
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

diagonal_elements = np.diagonal(matrix)
print("\nDiagonal Elements:", diagonal_elements)

def softmax(values):
    exp_values = np.exp(values - np.max(values))  #I dont know why e^max(values) is divided but thats what is saw on chatgpt
    return exp_values / np.sum(exp_values)

diagonal_softmax = softmax(diagonal_elements)
print("\nSoftmax of Diagonal Elements:", diagonal_softmax)

largest_diagonal_element = diagonal_elements[0]
for elem in diagonal_elements:
    if elem > largest_diagonal_element:
        largest_diagonal_element = elem

print("\nLargest Element on Principal Diagonal:", largest_diagonal_element)

plt.plot(diagonal_elements, diagonal_softmax, marker='o', color='b', label='Softmax')
plt.title("Softmax of Diagonal Elements")
plt.xlabel("Diagonal Elements")
plt.ylabel("Softmax Values")
plt.legend()
plt.show()
