number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

has_one = (first_digit == 1) or (second_digit == 1) or (third_digit == 1)

sum_digits = first_digit + second_digit + third_digit
is_sum_small = sum_digits < 12 

is_last_five = (third_digit == 5)

result = has_one and is_sum_small and is_last_five

print(result)
