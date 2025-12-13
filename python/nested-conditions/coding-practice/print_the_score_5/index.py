d = int(input())

if d <= 50:
    score = d * 3
elif d <= 100:
    score = 150 + (d - 50) * 5
elif d <= 200:
    score = 150 + 250 + (d - 100) * 6
else:
    sccore = 150 + 250 + 600 + (d - 200) * 10

score = score + 100

print(score)
