a,b = map(int, input().split())
while a < b:
    if a % 2 == 0:
        a += 3
    else:
        a *= 2
    print(a, end = ' ')
    