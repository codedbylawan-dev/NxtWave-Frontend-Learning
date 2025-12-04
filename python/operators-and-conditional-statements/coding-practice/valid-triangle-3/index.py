first_side = int(input())
second_side = int(input())
third_side = int(input())

is_greater_than_third_side = (first_side + second_side) > third_side
is_greater_than_first_side = (second_side + third_side) > first_side
is_greater_than_second_side = (third_side + first_side) > second_side

if is_greater_than_first_side and is_greater_than_second_side and is_greater_than_third_side:
    print("It's a Triangle")
else:
    print("It's not a Triangle")