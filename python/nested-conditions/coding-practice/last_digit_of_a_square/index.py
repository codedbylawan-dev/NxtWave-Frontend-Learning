n = int(input())

sq = n * n 

last_n = n % 10
last_sq = sq % 10

if last_n == last_sq:
    print("Equal")
else:
    print("Not Equal")