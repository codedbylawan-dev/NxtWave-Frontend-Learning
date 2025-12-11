n = int(input())

tens = n // 10
ones = n % 10

cond1 = (n % tens == 0)
cond2 = (ones != 0 and n % ones == 0)

if cond1 and cond2:
    print(n * 2)
else:
    print(n)
