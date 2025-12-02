a = int(input())
b = int(input())

sum_val = a + b 

diff_val = abs(a - b)

condition_1 = sum_val < 10 
condition_2 = diff_val < 10
condition_3 = (a > 5) and (a < 30)

result = condition_1 or condition_2 or condition_3
print(result)