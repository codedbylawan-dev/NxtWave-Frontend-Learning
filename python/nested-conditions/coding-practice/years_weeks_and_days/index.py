n = int(input())

y = n // 365

remaining = n % 365

w = remaining // 7
d = remaining % 7

print(y)
print(w)
print(d)