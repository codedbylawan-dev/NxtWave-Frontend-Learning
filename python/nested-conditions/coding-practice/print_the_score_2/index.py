d = int(input())

if d <= 50:
    score = d * 3
else:
    score = 50 * 3 + (d - 50) * 5

print(score)