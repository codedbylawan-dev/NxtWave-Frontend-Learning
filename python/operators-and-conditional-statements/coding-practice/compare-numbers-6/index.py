number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

all_digits_greater = (first_digit > 4) and (second_digit > 4) and (third_digit > 4)
first_digit_is_six = (first_digit == 6)

result = all_digits_greater or first_digit_is_six

print(result)
