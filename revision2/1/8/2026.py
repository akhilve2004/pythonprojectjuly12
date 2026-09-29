#print all 3 digit numbers using while loop
#initialisation
#while (condition)
#statement to excute
#incrementation

# i=100
# while i<=999:
#     print(i,end=" ,")
#     i+=1

#.................................................................................

#using for loop
# for i in range(100,1000):
#     print(i,end=" ,")
#..........................................................................................
#given a list of colours
colors=['red','green','blue','orange','yellow','black']
#print each colour
# for i in colors:
#     print(i)
##...................................................................................

#colors contain letter 'b'
# for i in colors:
#     if 'b'in i:
#      print(i)
#................................................................
#colours with letters starting letter g
# for i in colors:
#     if i[0]=='g':
#         print(i)
#................................................................
#colors end with e
# for i in colors:
#     if i[-1]=='e':
#         print(i)
#...........................................................
#first colour starting with b
# for i in colors:
#     if(i[0]=="b"):
#         print(i)
#         break
#......................................................
#all colors except colours starting with b
# for i in colors:
#     if(i[0]=="b"):
#         continue
#     print(i)
#................................................
l=[23,45,12,78,90,51,75]
#print all numbers
# for i in l:
#     print(i)
#.............................................
#print all even numbers
# for i in l:
#     if i%2==0:
#         print(i)
#.................................................
#print those numbers that are divisible by 5
# for i in l:
#     if i%5==0:
#      print(i)
#.........................................................
#stops the loop if i>50
# for i in l:
#     if i >50:
#         break
#     print(i)
#...........................................................
#skips all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)
#............................................................
#print the first even number whose value is greater than 50
# for i in l:
#     if i%2==0 and i>50:
#         print(i)
#         break
#................................................................
#count of all even numbers
# count=0
# for i in l:
#     if i%2==0:
#         count=count+1
# print(count)
#..............................................................
#sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print("sum",sum)
#..................................................
#product of odd numbers
# p=1
# for i in l:
#     if i%2!=0:
#         p=p*i
# print(p)
#.....................................................................
##looping
#print each digit in a number
# n=1234
# s=str(n)
# for i in s:
#     print(i)
#..................................................................
#sum of digits in a number
n=1234
s=str(n)
sum=0
for i in s:
    sum=sum+i
print(i)
