N, M = map(int, input().split())
print(N)
while N > 0 and N//M != 0:
    print(N//M)
    N=N//M

