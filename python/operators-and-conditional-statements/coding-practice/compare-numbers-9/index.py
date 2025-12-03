number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

is_greater = (first_digit > 7) and (second_digit > 7) and (third_digit > 7)

p1 = (first_digit * second_digit) <= 30
p2 = (second_digit * third_digit) <= 30
p3 = (third_digit * first_digit) <= 30

is_product_small = p1 and p2 and p3 

result = is_greater or is_product_small

print(result)
