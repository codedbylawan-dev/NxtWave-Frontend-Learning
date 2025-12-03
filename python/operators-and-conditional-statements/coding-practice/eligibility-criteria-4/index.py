m = int(input())
p = int(input())
c = int(input())

cond1 = (m >= 60) and (p >= 50) and (c >= 45) and (m + p + c >= 180)

cond2 = (m + p >= 120) or (c + p >= 110)

result = cond1 or cond2

print(result)