n = int(input())

greatest = int(input())

for i in range(1, n):
    number = int(input())
    if number > greatest:
        greatest = number

print(greatest)