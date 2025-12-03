a = int(input())
b = int(input())

sum_val = a + b 
product_val = a * b 

is_sum_negative = (sum_val < 0)
is_product_negative = (product_val < 0)

result = is_sum_negative or is_product_negative

print(result)