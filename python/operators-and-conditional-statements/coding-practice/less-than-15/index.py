a = int(input())
b = int(input())
c = int(input())

is_a_less = a < 15
is_b_less = b < 15
is_c_less = c < 15

result = is_a_less or is_b_less or is_c_less

print(result)
