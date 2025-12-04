string = input()

string_length = len(string)

is_between = (string_length >= 2) and (string_length <= 7)

is_not_equal = string[0] != "a"

if is_between or is_not_equal:
    print("Valid String")
else:
    print("Not a Valid String")