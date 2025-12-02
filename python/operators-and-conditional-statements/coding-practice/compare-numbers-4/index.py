first_number = int(input())
second_number = int(input())

is_less_than = (first_number < 60) or (second_number < 60)

is_greater_than = (first_number > 80) or (second_number > 80)

result = is_less_than and is_greater_than

print(result)
