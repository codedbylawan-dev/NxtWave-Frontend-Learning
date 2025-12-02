m = int(input())
p = int(input())
c = int(input())

condition_1 = (m >= 70) and (p >= 60) and (c >= 60)

total = m + p + c 

condition_2 = total >= 180

result = condition_1 or condition_2

print(result)