first_number = int(input())
second_number = int(input())

sum_of_numbers = first_number + second_number

is_negative = (first_number < 0) or (second_number < 0)

is_greater_than = sum_of_numbers > 7 

result = is_negative and is_greater_than

print(result)