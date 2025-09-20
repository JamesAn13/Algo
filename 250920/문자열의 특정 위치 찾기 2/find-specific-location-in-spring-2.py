a = str(input())
cnt = 0
n = ['apple', 'banana', 'grape', 'blueberry', 'orange']
for x in n:
    if a == x[2] or a == x[3]:
        print(x)
        cnt += 1
print(cnt)
