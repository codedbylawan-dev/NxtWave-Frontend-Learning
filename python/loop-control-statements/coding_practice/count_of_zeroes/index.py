n = input()

count = 0

for ch in n:
    if ch == "0":
        count += 1 

if count > 3:
    print("Count of zeros is greater than three")
else:
    print("Count of zeros is not greater than three")