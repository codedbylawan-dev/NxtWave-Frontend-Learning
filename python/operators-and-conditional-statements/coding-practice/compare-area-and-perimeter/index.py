length = int(input())
breadth = int(input())

area = length * breadth

perimeter = 2 * (length + breadth)

result = area <= perimeter

print(result)