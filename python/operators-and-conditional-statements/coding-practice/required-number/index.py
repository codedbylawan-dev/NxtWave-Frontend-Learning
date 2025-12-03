n = int(input())

is_between = (n > 50) and (n < 100)

first_digit = int(str(n)[0])

is_first_seven = (first_digit == 7)

result = is_between or is_first_seven

print(result)
