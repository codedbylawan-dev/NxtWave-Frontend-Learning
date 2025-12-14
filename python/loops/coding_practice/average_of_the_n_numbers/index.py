N = int(input())

sum_value = 0
count = 1

while count <= N:
    sum_value = sum_value + count
    count = count + 1

average = sum_value / N
print(average)