a = int(input())
b = int(input())
c = int(input())

sum_ab = a + b 
sum_bc = b + c 
sum_ca = c + a 

is_ab = sum_ab > 10
is_bc = sum_bc > 10
is_ca = sum_ca > 10

result = is_ab and is_bc and is_ca

print(result)