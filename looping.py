#write a program to print first 10  integers

# i=1
# while i<=10:
#     print(i,end=" ,")
#     i+=1

#write a program to print first 10 even numbers

# i=2
# while i<=20:
#     print(i,end=" ,")
#     i+=2

#write a program to print first 10 odd numbers

# i=1
# while i<=19:
#   print(i,end=" ,")
#   i+=2

#1,4,7,10,13,16 print

# i=1
# while i<=16:
#     print(i,end=" ,")
#     i+=3

#10,20,30,40,50,60,60,80 print

# i=10
# while i<=80:
#   print(i,end=" ,")
#   i+=10

#3,6,9,12,15,18,21 print

# i=3
# while i<=21:
#  print(i,end=" ,")
#  i+=3

#5,4,3,2,1 print
# i=5
# while i>=1:
#  print(i,end=" ,")
#  i-=1

#8,6,4,2,0 print
# i=8
# while i>=0:
#     print(i,end=" ,")
#     i-=1

#100.101,102,......200 print

# i=100
# while i<=200:
#     print(i,end=" ,")
#     i+=1

#print all 4 digits number(1000-9999)

# i=1000
# while i<=9999:
#     print(i,end=" ,")
#     i+=1

#print those 3 digits numbers  that are divisible by 3

# i=100
# while i<=999:
#     if i %3==0:
#         print(i,end=" ,")
#     i+=1

#print those 4 digit numbers that contains digit '3' (#in operator sequence)

# i=1000
# while i<=9999:
#     s=str(i)
#     if '3' in s:
#         print(s,end=" ,")
#     i+=1

#print those numbers that are divisible by 3 and 5 in the range (1,100)
#
# i=1
# while i<=100:
#    if i%3==0 and i%5==0:
#         print(i,end=" ,")
#    i+=1

#1,4,9,16,25,36,49,64,81,100 print

# i=1
# while i<=10:
#     print((i**2),end=", ")
#     i+=1

#print those 3 digit numbers that containing digit 3


#30/07/2026...................

#count of those 3 digit numbers  that contain digit '3'


# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if '3' in s:
#         count=count+1
#     i+=1
# print(count)

#count of those numbers that are divisible by 7 or 3 in the range(200,300)

# count=0
# i=200
# while i<=300:
#     if i%7==0  or i%3==0:
#         count=count+1
#     i+=1
# print(count)

#count of odd numbers that are divisible by 5 in the range (1,100)

# count=0
# i=1
# while i<=100:
#     if i%5==0 and i%2!=0:
#         count=count+1
#     i+=1
# print(count)

#count of all palindrome number in the range (1,1000)

# count=0
# i=1
# while i<=1000:
#     s=str(i)
#     if s==s[::-1]:
#         count=count+1
#     i+=1
# print(count)

#count the number divisible by 3 in the range(1,50)
# count=0
# i=1
# while i<=50:
#     if i%3==0:
#         count=count+1
#     i+=1
# print(count)

#SUM....................................................................................

#find the sum of first 5 numbers 1+2+3+4+5
# s=0
# i=1
# while i<=5:
#     s+=i
#     i+=1
# print(s)

#sum of those numbers that are divisible by 3 in the range (1,50)

# s=0
# i=1
# while i<=50:
#     if i%3==0:
#         s+=i
#     i+=1
# print(s)

#sum of all 3 digits numbers

# s=0
# i=100
# while i<=999:
#     s+=1
#     i+=1
# print(s)

#sum of first 10 even numbers

# s=0
# i=2
# while i<=20:
#     s+=2
#     i+=2
# print(s)

#PRODUCT.................................................................................................

#product of series 1,2,3,4,5 (product varialbe initialized by 1  i.e product=1  product=product*i)

# product=1
# i=1
# while i<=5:
#     product*=i
#     i+=1
# print(product)


#product of first 10 odd numbers

product=1
# i=1
# while i<=19:
#     if i%2!=0:
#
#       product*=i
#     i+=1
# print(product)


#product of numbers that contain digit 3 in the range(1,50)
# product=1
# i=1
# while i<=50:
#     if '3'in str(i):
#         product=product*i
#     i+=1
# print(product)

#factorial of a number entered by a user.......................................................

# n=int(input("enter a number:"))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)

#multiplication table of a number...upto 10 number
# n=int(input("enter a number to print table:"))
# i=1
# p=1
# while i<=10:
#     p=p*i
#     print(f"{i} * {n} = {n*i}")
#     i=i+1

#sum of digits of a number........135=1+3+5..
# n=int(input("enter number"))
# s=0
# while n>0:      #135   13>0  1>0  0>0
#     d=n%10      #5     13%10=3  1%10=1
#     s=s+d       #0+5=5 5+3=8 8+1=9
#     n=n//10     #135//10=13  13//10
# print(s)
