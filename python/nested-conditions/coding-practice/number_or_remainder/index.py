n = int(input())

cond1 = (n % 5 == 0) and (n % 7 == 0)
cond2 = (n < 7)

if cond1 or cond2:
    print(n)
else:
    print(n % 5)
    print(n % 7)