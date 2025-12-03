a = int(input())
b = int(input())
c = int(input())

is_a_valid = a >= 20
is_b_valid = b >= 20
is_c_valid = c >= 20

result = is_a_valid and is_b_valid and is_c_valid

print(result)