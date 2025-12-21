n = int(input())

smallest = int(input())

for i in range(n - 1):
    number = int(input())
    if number < smallest:
        smallest = number

print(smallest)