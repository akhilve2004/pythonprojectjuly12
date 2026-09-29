#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

# weight=float(input("enter the weight in kg:"))
# height=float(input("enter the height in meters:"))
# bmi= weight  / height**2
# print("Your bmi is:",round(bmi,2))
# if bmi<=18.4:
#     print("under weight:")
# elif 18.5<= bmi <=24.9:
#     print("normal")
# elif 25.0<=bmi <=39.9:
#     print("over weight")
# else:
#     print("obese")

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# code=int(input("enter product code(1-battery,2-key,3-electrical):"))
# amount=float(input("enter order amount(Rs.):"))
# discount=0
# if code==1:
#     if amount>1000:
#         discount =0.10* amount
#
# elif code ==2:
#     if amount>100:
#         discount=0.05*amount
# elif code ==3:
#     if amount>500:
#         discount=0.10*amount
# else:
#     print("invalid product")
#
# net_amount=amount-discount
#
# print("discount: Rs.",discount)
# print("net amount to pay:Rs.",net_amount)

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# n=int(input("enter a number:"))
# if n%3==0 and n%5==0:
#   print("fizzbuzz")
# elif n%3==0 and n%5!=0:
#     print("fizz")
# elif n%5==0 and n&3!=0:
#   print("buzz")
# else:
#     print(f"{n}")




