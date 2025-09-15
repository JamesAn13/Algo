string = input().split()
if len(string[0]) > len(string[1]):
    print(string[0], len(string[0]))
elif len(string[0]) == len(string[1]):
    print('same')
else: 
    print(string[1], len(string[1]))