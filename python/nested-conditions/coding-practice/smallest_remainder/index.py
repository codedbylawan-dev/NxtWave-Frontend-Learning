a = int(input())
b = int(input())

r1 = a % b 
r2 = b % a 

if r1 < r2:
    print(r1)
else:
    print(r2)
