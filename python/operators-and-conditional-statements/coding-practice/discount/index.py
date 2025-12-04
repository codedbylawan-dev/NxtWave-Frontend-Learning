coupon_1 = input()
coupon_2 = input()

first_three_a = coupon_1[0:3]
first_three_b = coupon_2[0:3]

is_discount = (first_three_a == "DIS") or (first_three_b == "DIS")

if is_discount:
    print("Discount")
else:
    print("No Discount")
    