a = int(input())
b = int(input())

is_any_number_has = (a == 6) or (b == 6)

is_sum_equal_to_6 = (a + b) == 6

is_diff_equal_to_6 = (a - b == 6) or (b -a == 6)

if is_any_number_has or is_sum_equal_to_6 or is_diff_equal_to_6:
    print("Lucky")
else:
    print("Not Lucky")
    