number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

result = (first_digit == 0) or (second_digit == 0) or (third_digit == 0)

print(result)