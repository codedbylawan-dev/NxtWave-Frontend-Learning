a = int(input())
b = int(input())
c = int(input())

cond1 = (a + b) > c 
cond2 = (b + c) > a 
cond3 = (c + a) > b 

result = cond1 and cond2 and cond3

print(result)