a = int(input())
b = int(input())

sum_val = a + b 

sum_digits = len(str(sum_val))

is_sum_valid = sum_digits < 3

product_val = a * b 

product_digits = len(str(product_val))
is_product_valid = product_digits < 3 

result = is_sum_valid and is_product_valid

print(result)