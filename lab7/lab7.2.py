import random

def generate_matrix(m, n, min_val, max_val, is_float=False):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            if is_float:
                row.append(round(random.uniform(min_val, max_val), 2))  # Дійсні числа
            else:
                row.append(random.randint(min_val, max_val))  # Цілі числа
        matrix.append(row)
    return matrix

def find_min_max_rows(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    min_row_idx = max_row_idx = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row_idx = i
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row_idx = i
    return min_row_idx, max_row_idx

def swap_rows(matrix, row1_idx, row2_idx):
    matrix[row1_idx], matrix[row2_idx] = matrix[row2_idx], matrix[row1_idx]

def print_diagonals(matrix):
    n = len(matrix)
    print("Головна діагональ:", [matrix[i][i] for i in range(n)])
    print("Побічна діагональ:", [matrix[i][n-i-1] for i in range(n)])

n = len(input("Введіть своє ім'я: "))  # Кількість літер в імені
m = len(input("Введіть своє прізвище: "))  # Кількість літер в прізвищі

matrix = generate_matrix(m, n, 0, 20)

print("Початкова матриця:")
for row in matrix:
    print(row)

min_row_idx, max_row_idx = find_min_max_rows(matrix)

swap_rows(matrix, min_row_idx, max_row_idx)

print("\nМатриця після зміни рядків (максимальний і мінімальний рядки):")
for row in matrix:
    print(row)

print_diagonals(matrix)