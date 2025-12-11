n = int(input())

tens = n // 10
ones = n % 10

cond1 = (n % 9 == 0)
cond2 = (tens == 9)
cond3 = (ones == 9)

if cond1 or cond2 or cond3:
    print("Lucky Number")
else:
    print("Unlucky Number")
    