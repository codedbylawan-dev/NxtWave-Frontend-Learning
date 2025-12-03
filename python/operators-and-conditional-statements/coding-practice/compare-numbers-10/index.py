a = int(input())
b = int(input())

is_less_than_20 = (a < 20) or (b < 20)

is_greater_than_30 = (a > 30) or (b > 30)

result = is_less_than_20 and is_greater_than_30

print(result)