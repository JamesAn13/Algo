# arr1 = [
#     list(map(int, input().split()))
#     for _ in range(3)
# ]
# input()
# arr2 = [
#     list(map(int, input().split()))
#     for _ in range(3)
# ]
# arr3=[]

# for i in range(3):
#     rowlist = []
#     for j in range(3):
#         result = arr1[i][j] * arr2[i][j]
#         rowlist.append(result)
#     arr3.append(rowlist)

# for row in arr3:
#     for elem in row:
#         print(elem, end = ' ')
#     print()
arr1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()
arr2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

# 💡 한 줄로 두 배열의 요소별 곱셈을 수행합니다.
arr3 = [
    [arr1[i][j] * arr2[i][j] for j in range(3)] 
    for i in range(3)
]

for row in arr3:
    for elem in row:
        print(elem, end=' ')
    print()