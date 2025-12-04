room_number = input()

number = room_number[1:]
number = int(number)

if number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")
    