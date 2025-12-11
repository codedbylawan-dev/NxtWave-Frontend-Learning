a = int(input())
b = int(input())

pow1 = a ** b
pow2 = b ** a 

if pow1 > pow2:
    print(pow1)
else:
    print(pow2)