s = str(input())
n = s.replace(s[1], 'a', 1)
n = n.replace(s[-2], 'a', 1)
print(n)