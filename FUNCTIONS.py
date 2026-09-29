#FUNCTIONS............

# def add():
#     "addition of two numbers"
#
#     n1=int(input("enter number"))
#     n2=int(input("enter number"))
#     s=n1+n2
#     print("sum",s)
#     return
# add()

#define a function to display "hello your name "
#define a function to find the count of a specific character in a string
#define a function to find the factorial of a number


# def hello():
#     name=(input("enter your name"))
#     print("hello",name)
#     return
# hello()
#
# def count_ch():
#     count=0
#     s=input("enter the string")
#     ch=input("enter the character")
#     for i in s:
#         if(i==ch):
#             count=count+1
#     print(count)
#     return
# count_ch()


# def fact():
#     n=int(input("enter number"))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print("factorial",f)
# fact()


#define a function to check whether a number is armstrong or not
#define a function to check whether a number is prime or nor
# def check_armstrong():
#     n=int(input("enter number"))
#     s=str(n)
#     sum=0
#     l=len(s)
#     for i in s:
#         s=s+int(i)**l
#     if (sum==n):
#         print("Armstrong")
#     else:
#      print("Not armstrong")



#...........................................
# def check_prime(n):
#     if n <= 1:
#         print("Not Prime")
#         return
#
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             return
#
#     print("Prime")
# num = int(input("Enter a number: "))
# check_prime(num)


#define a function to find factors of a number
# def find_factors(n):
#     print("Factors are:")
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i)
# num = int(input("Enter a number: "))
# find_factors(num)



#............
# def factors():
#     "facors of a number"
#     n=int(input("enter the number"))
#     for i in range(1,n+1):
#         if(n%i==0):
#             print(i)
#     return
# factors()     #calling

#definr a function that take 2 arguments and print the sum
# def add(n1:{_add_},n2):
#     s=n1+n2
#     print
#define a function that takes 3 arguments and find the simple interest(dynamic input)
#simple interest+(principal amount*years*rate)/100
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (years): "))


def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest =", si)