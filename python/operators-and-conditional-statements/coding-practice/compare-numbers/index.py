first_number = int(input())
second_number = int(input())

are_greater_than = (first_number > 35) and (second_number > 35)

is_first_number_greater = first_number > second_number

result = are_greater_than or is_first_number_greater

print(result)
