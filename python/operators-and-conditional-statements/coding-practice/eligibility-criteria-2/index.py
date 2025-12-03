m = int(input())
p = int(input())
c = int(input())

sum_mp = m + p 
sum_pc = p + c 
sum_cm = c + m 

pair_condition = (sum_mp >= 100) or (sum_pc >= 100) or (sum_cm >= 100)

total = m + p + c 

total_condition = total >= 180 

result = pair_condition and total_condition

print(result)