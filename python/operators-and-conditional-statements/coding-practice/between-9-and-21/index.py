a = int(input())
b = int(input())
c = int(input())

is_a_between = (a > 9) and (a < 21)
is_b_between = (b > 9) and (b < 21)
is_c_between = (c > 9) and (c < 21)

result = is_a_between or is_b_between or is_c_between

print(result)
