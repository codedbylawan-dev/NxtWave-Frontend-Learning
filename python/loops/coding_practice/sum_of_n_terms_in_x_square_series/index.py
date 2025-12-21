x = input()
n = int(input())

term = ""

total = 0

for i in range(n):
    term = term + x 
    number = int(term)
    total = total + (number * number)

print(total)