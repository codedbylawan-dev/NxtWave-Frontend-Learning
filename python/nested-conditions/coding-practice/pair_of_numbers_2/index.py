a = int(input())
b = int(input())

cond1 = (a % 3 == 0 and b % 3 == 0)
cond2 = (a % 12 == 0 or b % 12 == 0)

if cond1 and cond2:
    print("Pair")
else:
    print("Not a Pair")
    