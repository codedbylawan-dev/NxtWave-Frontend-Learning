first_number = int(input())
second_number = int(input())

is_less_than_or_equal_to = (first_number <= 1000) and (second_number <= 1000)

is_greater_than = second_number > 500

is_pair = is_less_than_or_equal_to or is_greater_than

if is_pair:
    print("Pair")
else:
    print("Not a Pair")
    