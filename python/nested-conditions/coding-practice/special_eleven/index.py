n = int(input())

remainder = n % 11

if remainder == 0 or remainder == 1:
    print("Special Eleven")
else:
    print("Normal Number")
    