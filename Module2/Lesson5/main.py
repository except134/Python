def get_matrix(n, m, value):
    matrix = [0] * n 
    for nn in range(n):
        matrix[nn] = [0] * m
        for mm in range(m):
            matrix[nn][mm] = value
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(0, 2, 13)
result5 = get_matrix(4, 0, 13)
result6 = get_matrix(0, 0, 13)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)


