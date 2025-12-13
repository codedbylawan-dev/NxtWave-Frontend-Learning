n = int(input())

rem = n % 6 

if rem == 0:
    print("Group 6")
else:
    print("Group " + str(rem))