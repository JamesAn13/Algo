a = []  
t = 0
f = 0
for i in range (10):
    b = int(input())
    a.append(b)
for x in a:
    if x % 15 == 0:
        t += 1
        f += 1
    elif x % 3 == 0:
        t += 1
    elif x % 5 == 0:
        f += 1
    else:
        continue

print(t, f)