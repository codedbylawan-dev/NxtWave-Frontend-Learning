m = int(input())
p = int(input())
c = int(input())

all_pass = (m >= 35) and (p >= 35) and (c >= 35)

pair_sum_ok = (m + p >= 90) or (p + c >= 90) or (m + c >= 90)

result = all_pass and pair_sum_ok

print(result)