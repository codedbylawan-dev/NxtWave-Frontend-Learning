N = int(input())

a = N // 100        # hundreds digit
b = (N // 10) % 10  # tens digit
c = N % 10          # ones digit

sum_cubes = (a ** 3) + (b ** 3) + (c ** 3)

if sum_cubes == N:
    print("True")
else:
    print("False")
