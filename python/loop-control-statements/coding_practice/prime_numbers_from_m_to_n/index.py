m = int(input())
n = int(input())

found = False

for num in range(m, n + 1):
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print(num, end=" ")
            found = True

if found == False:
    print("No Prime Numbers Found")
