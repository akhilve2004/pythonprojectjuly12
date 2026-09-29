# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# print numbers divisible by 3 or 5 from 1 to 100

# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)

#.....................................................................................................

# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# n=[1,2,3,4]
# cumulative=[]
# total=0
# for i in n:
#     total=total+1
#     cumulative.append(total)
#     print(cumulative)

#......................................................................................................# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
#
# a=3
# b=7
# total=0
# for i in range(a,b+1):
#     total=total+i
#     print(total)

#..
# ........................................................................................................
# 4.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90

# for i in range(0,len(l)):
#     print(l[i])

# l=[10,20,30,40,50]
# total=0
# for i in range(0,len(l)):
#     if i%2==0:
#         total+=l[i]
#         print(total)
#.................................................................................................................

#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
l=[4,9,1,0,6,7]
#
# total = 0
#
# for i in l:
#     if i == 0:
#         break
#     total += i
#
# print(total)
#................................................................................................
# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1, 1001):
#     if i % 7 == 0 and i % 11 == 0:
#         print(i)
#         break
#.................................................................................................
# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# l = ["apple", "bat", "orange", "cat", "grapes", "dog"]
#
# for word in l:
#     if len(word) < 5:
#         continue
#     print(word)

#......................................................................................................
#8.From a list of numbers, create a new list containing the squares of each element.
# # Input: [1, 2, 3] → Output: [1, 4, 9]
# nums = [1, 2, 3]
#
# squares = []
#
# for n in nums:
#     squares.append(n * n)
#
# print(squares)
#......................................................................................................
# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# s = "hello world"

#result = ""

# for ch in s:
#     if ch.lower() in "aeiou":
#         continue
#     result += ch
#
# print(result)
#......................................................................................................

# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l = [5, 2, 8, 6, 2]
#
# result = []
#
# for n in l:
#     doubled = n * 2
#
#     if doubled > 50:
#         break  # stop if doubled value exceeds 50
#
#     result.append(doubled)
#
# print(result)
#........................................................................................................
# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
# s = "abc123x7z"
#
# result = ""
#
# for ch in s:
#     if ch.isdigit():
#         result += ch
#
# print(result)
#......................................................................................................
# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
#
#
# nums = [4, -3, 2, -1]
#
# result = []
#
# for n in nums:
#     if n < 0:
#         result.append(0)
#     else:
#         result.append(n)
#
# print(result)
#..............................................................................................
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students

# for i in d.values:
# #    print(i[0])
# d = {
#     101: ['Arun', 23, 'ekm'],
#     102: ['Amal', 25, 'tvm'],
#     103: ['Anu', 26, 'tcr'],
#     104: ['Kiran', 27, 'ekm']
# }
#
# for i in d.values():
#     print(i[0])
#................................................................................................
#Write a program to print the numbers from 1 to 100.
# But for multiples of:
#
# 3, print “Fizz” instead of the number
#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# Otherwise, print the number itself
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#.......................................................................................................
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break
# for i in range(1, 51):
#     if i > 40:
#         break
#
#     if i % 5 == 0:
#         continue
#
#     print(i)
###################################.......................
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number


#
# num = 1234   # you can change this number
#
# reverse = 0
# count = 0
# total = 0
#
# temp = num   # store original number
#
# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     total += digit
#     count += 1
#     temp = temp // 10
#
# print("Reverse:", reverse)
# print("Count of digits:", count)
# print("Sum of digits:", total)
