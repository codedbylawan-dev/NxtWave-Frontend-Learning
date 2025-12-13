units = int(input())
bill = 0

if units <= 50:
    bill = units * 2
else:
    bill += 50 * 2
    units -= 50

    if units <= 100:
        bill += units * 3
    else:
        bill += 100 * 3
        units -= 100

        if units <= 100:
            bill += units * 5
        else:
            bill += 100 * 5
            units -= 100

            bill += units * 8

bill = bill + (bill * 0.2)
print(float(bill))