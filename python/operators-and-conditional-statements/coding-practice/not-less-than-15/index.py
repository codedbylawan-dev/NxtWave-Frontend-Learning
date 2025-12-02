a = int(input())
b = int(input())

is_a_not_less = a >= 15
is_b_not_less = b >= 15

result = is_a_not_less or is_b_not_less

print(result)