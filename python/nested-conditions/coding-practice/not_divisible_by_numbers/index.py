n = int(input())

cond = (n % 2 != 0) and (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0)

if cond:
    print("True")
else:
    print("False")