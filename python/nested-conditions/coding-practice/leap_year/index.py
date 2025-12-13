Y = int(input())

cond1 = (Y % 400 == 0)
cond2 = (Y % 4 == 0) and (Y % 100 != 0)

if cond1 or cond2:
    print("True")
else:
    print("False")
    