n = int(input())

sum_values = 0
counter = 0

while counter < n:
    num = int(input())
    sum_values = sum_values + num
    counter = counter + 1

average = sum_values/n
print(average)