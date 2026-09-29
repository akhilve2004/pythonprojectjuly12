#write a program to check whether the user entered number is a positive even or odd / negative even or odd

# num=int(input("enter a number:"))
# if num>0: #26   -23
#     print("positive")
#     if num%2==0: #26%2==0
#         print("even")
#     else:
#         print("odd")
# else:
#     print("negative")
#     if num%2!=0: #25%2!=0
#         print("odd")
#     else:
#         print("even")


#check whether a number is
# divisible by 2 and 3
# /divisible by 2 and not by 2
# /divisible by 3 and not by 2
#not divisible by 2 and 3

num=int(input("enter a number"))
if num%2==0:
    print("divisible by 2")
    if num%3==0:
        print("divisible by 3")
    else:
        print("not divisible by 3")
else:
    print("not divisible by 2")
    if num%3==0:
        print("divisible by 3")
    else:
        print("not divisible by 3")
