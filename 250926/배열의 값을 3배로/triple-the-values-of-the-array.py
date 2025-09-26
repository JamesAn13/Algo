# matrix = []
# for i in range(3):
#     row_data = list(map(int, input().split()))
#     matrix.append(row_data)

# new_matrix = []
# for i in range(3):
#     new_row = []
#     for j in range(3):
#         new_row.append(matrix[i][j] * 3)
#     new_matrix.append(new_row)

# for i in range(3):
#     for j in range(3):
#         print(new_matrix[i][j], end=" ")
#     print()
arr = [
	list(map(int, input().split()))
	for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr[i][j] *= 3
	
for row in arr:
	for elem in row:
		print(elem, end=" ")
	print()

