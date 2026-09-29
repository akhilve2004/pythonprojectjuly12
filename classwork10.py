



# try:
#     n=int(input("enter a number"))
#     r=math.factorial(n)
#     print("factorial",r)
#
# except:
#     print("invalid input")






try:
    n=int(input("enter number"))
    m=int(input("enter a number"))

    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")

    ch=int(input("enter your choice"))

    if ch==1:
        print("Result",n+m)
        