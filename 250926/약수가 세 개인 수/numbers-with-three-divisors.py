start, end = map(int, input().split())
tcnt = 0
for i in range(start, end+1):
    scnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            scnt+=1
    if  scnt == 3:
        tcnt +=1
print(tcnt)


