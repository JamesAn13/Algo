s = input()

l = len(s)

s = s[:1] + 'a' + s[2:]
s = s[:l -2] + 'a' + s[l-1:]

print(s)