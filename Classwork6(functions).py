# # # Q1.Define a function that takes 2 numbers and returns their product
#
# # Q2.Define a function that takes a string and returns number of vowels
#
# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]

#Q1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def product(a, b):
#     return a * b
# print(product(a, b))
# product


#.................................................................
# #Q2
# s = input("Enter a string: ")
# def count_vowels(s):
#     count = 0
#
#     for i in s:
#         if i in "aeiouAEIOU":
#             count += 1
#
#     return count
# print(count_vowels(s))
# count




# l = int(input("Enter length: "))
# b = int(input("Enter breadth: "))
# def area(length, breadth):
#     return length * breadth
#
# print(area(l, b))
# area()






# def even_numbers(l):
#     new = []
#
#     for i in l:
#         if i % 2 == 0:
#             new.append(i)
#
#     return new
#
#
# l = [45, 78, 90, 12, 35]
#
# print(even_numbers(l))

#
#
# l = [123, 345, 111, 678, 134, 809]
# def digit_sum(l):
#     new = []
#
#     for i in l:
#         sum = 0
#
#         while i > 0:
#             rem = i % 10
#             sum = sum + rem
#             i = i // 10
#
#         new.append(sum)
#
#     return new
#
#
# l = [123, 345, 111, 678, 134, 809]
#
# print(digit_sum(l))



#
# def unique_elements(l):
#     new = []
#
#     for i in l:
#         if i not in new:
#             new.append(i)
#
#     return new
#
#
# l = [12, 34, 78, 12, 67, 34, 90, 23]
#
# print(unique_elements(l))

#
#
# def common_elements(list1, list2):
#     new = []
#
#     for i in list1:
#         if i in list2:
#             new.append(i)
#
#     return new
#
#
# list1 = [12, 34, 56, 78, 90]
# list2 = [90, 34, 11, 57, 45]
#
# print(common_elements(list1, list2))