n = input()
k = len(n)

total = 0

for digit in n:
    number = int(digit)
    total = total + (number ** k)

if total == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")