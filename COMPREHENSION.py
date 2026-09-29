#given a list
# l=[1,2,3,4]
# #create a new list with square of each element
# new=[i**2 for i in l ]#in eaxh itration adds i**2 where i akes values from the sequence l
# print(new)
# new=[i**3 for i in l]# in each itreation adss I**3 where i take value from the secquence l
# print(new)
# new=[5 for i in l]#in each itration adds
# print(new)

#..................................................................
#given a list
l=[23,46,55,11,78,90,24]
#create a new list with even values
# new=[]
# for i in l:
#     if(i%2==0):
#         new.append(i)
#     print(new)

# new=[i for i in l if i%2==0]
# print(new)

#create a new list with number greater than 50
# new=[i for i in l if i>50]
# print(new)
#.......................................................
#Given  a list
# colors=['red','green','blue','orange']
# create a new list with first letter of each color
# create a new list with length of each color
# first_letters = [i[0] for i in colors]
# print(first_letters)
# lengths = [len(i) for i in colors]
# print(lengths)

# #................................................................
# #create a new list of cubes
# l=[1,2,3,4]
# new=[i**3 for i in l ]
# print(new)
#create a new list of square roots
#l=[25,36,81,100]
# import math
#
# l = [25,36,81,100]
# sq_root = [math.sqrt(i) for i in l]
# print(sq_root)


#create a new list of lengths
#colors=['red','green','blue','yellow','black']
#create a new list of first characters
#create a new list of last characters
#create a new list of reverse of each elemnt
# colors = ['red','green','blue','yellow','black']
#
# lengths = [len(i) for i in colors]
# first_char = [i[0] for i in colors]
# last_char = [i[-1] for i in colors]
# reverse = [i[::-1] for i in colors]
#
# print(lengths)
# print(first_char)
# print(last_char)
# print(reverse)
#Given a list l=[23,78,12,56]
#Add 10 to each element in the given sequence
# l = [23,78,12,56]
# new_list = [i+10 for i in l]
# print(new_list)


##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]


#


# # #create a new list with square root of each element
# # l=[25,16,9,36]
# import math
#
# l = [25,16,9,36]
# sq_root = [math.sqrt(i) for i in l]
# print(sq_root)


# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
# # create a list of marks
# d = {'arun':25,'amal':34,'akhil':26,'anu':21}
#
# names = [i for i in d.keys()]
# marks = [i for i in d.values()]
#
# print(names)
# print(marks)
# #

# #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
# #create a list of floats
# #create a list of positive numbers
# l = [23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # new = [i for i in l if type(i)==str]
# print(new)
# # new = [i for i in l if type(i)==float]
# print(new)
# #  new= [i for i in l if type(i)!=str and i > 0]
# # print(new)


#
#
# #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# fruits = ['apple','orange','pineapple','avocado','grapes']
#
# long_fruits = [i for i in fruits if len(i) > 6]
# print(long_fruits)
# #create a new list with elements whose length is greater than 6

# #create a new list with elements whose value is divisible by 3 in range(1,101)

# Given s="python coding  is easy and fun"
# # create a new list with only vowels
s="python coding  is easy and fun"
new=[i for i  in s if i in "aeiouAEIOU"]
print(new)

#SET COMPREHENSION

#new={output for item in iterabble



