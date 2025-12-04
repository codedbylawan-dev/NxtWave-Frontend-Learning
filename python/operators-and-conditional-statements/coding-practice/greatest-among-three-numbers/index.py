a = int(input())
b = int(input())
c = int(input())

if a > b:
    greatest_number = a 
else:
    greatest_number = b 

if c > greatest_number:
    greatest_number = c 

print(greatest_number)
