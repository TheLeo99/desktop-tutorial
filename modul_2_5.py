def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list = []
        for j in range(m):
            list.append(value)
        matrix.append(list)
    return matrix
result1 = get_matrix(4, 2, 9)
result2 = get_matrix(2, 5, 16)
result3 = get_matrix(3, 3, 1)
print(result1)
print(result2)
print(result3)
