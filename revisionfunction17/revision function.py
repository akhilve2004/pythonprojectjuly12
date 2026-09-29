#define a function that takes a lis of numbers as arguments and print the count of even numbers, odd numbers and numbers whose values greater than 50
# l=[23,56,12,78,98,89,31,67]
# #even numbers..............................
# def count_numbers(l):
#     even = 0
#     odd = 0
#     greater = 0
#
#     for i in l:
#         if i%2 == 0:
#             even+= 1
#         else:
#             odd += 1
#         if i>50:
#             greater +=1
#     print("Even numbers:",even)
#     print("Odd numbers:",odd)
#     print("numbers greater than 50:",greater)
# l=[23,56,12,78,98,89,31,67]
# count_numbers(l)

#
# #using elif
# l=[23,56,12,78,98,89,31,67]
# def count_num(l):
#     even =0
#     odd =0
#     greater=0
#     for i in l:
#         if(i%2==0):
#             even+=1
#             if(i>50)
#                 greater +=1
#
#     print("ODD",odd)
#     print("EVEN",even)
#     print("GREATER",greater)

#define a function that take a list of words as arguments and return a new list of lengths
l=["red","green","orange","yellow","blue"]

d=[]
def color(l):
    for i in l:
        d.append(len(i))
    return d
a=color(l)
print(a)