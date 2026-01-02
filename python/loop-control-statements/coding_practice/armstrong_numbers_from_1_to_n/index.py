n = int(input())

for num in range(1, n + 1):
    temp = num
    count = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** count)
        temp = temp // 10

    if total == num:
        print(num)
