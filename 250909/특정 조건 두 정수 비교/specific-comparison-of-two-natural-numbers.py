a, b = map(int, input().split())
a1 , a2 = 0 , 0

if a < b:
    a1 = 1
else:
    a1 = 0

if a == b:
    a2 = 1
else:
    a2 = 0

print(a1, a2)
