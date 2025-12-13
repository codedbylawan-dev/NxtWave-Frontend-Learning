d = int(input())

if d <= 20:
    score = d * 2
elif d <= 60:
    score = 20 * 2 + (d - 20) * 4
else:
    score = 20 * 2 + 40 * 4 + (d - 60) * 6

total_score = score + 30
print(total_score)