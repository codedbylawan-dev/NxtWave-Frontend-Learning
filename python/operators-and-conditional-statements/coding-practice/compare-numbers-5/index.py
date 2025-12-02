a = int(input())
b = int(input())

product = a * b 

is_negative = (a < 0) or (b < 0)

is_product_valid = product >= -46

result = is_negative and is_product_valid

print(result)