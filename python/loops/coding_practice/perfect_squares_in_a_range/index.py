a = int(input())
b = int(input())

count = 0

for i in range(1, b + 1):
    square = i * i 
    if square >= a and square <= b:
        count = count + 1

print(count)