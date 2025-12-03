a = input()

is_above = int(a) > 25

first_digit = int(a[0])
second_digit = int(a[1])

is_greater = first_digit > second_digit

result = is_above and is_greater

print(result)