# n = int(input())

# for i in range (1, n+1):
#     for j in range (i):
#         i += 1
#         print(i, end= ' ')
#     print()

n = int(input())
cnt = 1
for i in range (1, n+1):
    for j in range (i):
        print(cnt, end= ' ')
        cnt+=1
    print()