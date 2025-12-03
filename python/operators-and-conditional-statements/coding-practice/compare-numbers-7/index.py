number = input()

first_two = int(number[:2])
last_two = int(number[-2])

check_first = (first_two == 19)
check_last = (last_two > 30) and (last_two < 60)

result = check_first and check_first

print(result)