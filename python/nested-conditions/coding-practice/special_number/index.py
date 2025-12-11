n = int(input())

tens = n // 10
ones = n % 10

sum_digits = tens + ones

cond1 = (sum_digits == 7)
cond2 = (tens == 7 or ones == 7) 
cond3 = (n % 7 == 0)

if cond1 or cond2 or cond3:
    print("Special Number")
else:
    print("Normal Number")
