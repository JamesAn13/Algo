y = int(input())

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('true')
        else:
            print('false')
    else:
        print('true')
else:
    print('false')

# year = int(input())

# if (year % 100 == 0) and (year % 400 != 0):
#     print("false")
# elif year % 4 != 0:
#     print("false")
# else: 
#     print("true")
