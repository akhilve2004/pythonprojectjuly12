# #given a list
# l=[1,1,2,3,4,5,5,6,7]
# #create a new dictionary where keys are numbers and values are count of each numbers
# new={}
# for i in l:
#     new[i]=l.count(i)
# print(new)
# dict[keyname]=value#given a list
# l=[1,1,2,3,4,5,5,6,7]
# #create a new dictionary where keys are numbers and values are count of each numbers
#
#
#given a list
l=[34,12,56,80,90,11]
#find the largest element
#find the second largest element
#find the smallest element
#find the second smallest element
# print("maximum",max(l))
# print("minimum",min(l))
#
# l.sort()
# print("sorted",l)
# print("second maximum",l[-2])

# print("second minimum",l[1])
#
# l=[['arun',23,40000],['amal',24,50000],['anu',27,30000]]
# # create a new list of salaried
# # create a new list of salaries,
# # find the maximum salary
# #
# # create a new list ages find the minimum age
#
# new=[]
# for i in l:
#     new.append(i[2])
# max(new)
#
# new=[]
# for i in l:
#     new.append(i[1])
# min(new)

###     SET #####.....................................................

# # 1.given a list
# # l=[1,1,1,2,3,3,4,5]
# # remove duplicate elements
# # l=list(set(l))
# # print(l)
# # 1.Given a list l=[1,1,1,2,3,3,4,5]
# #
# # remove duplicates from list
# #
# #
# # 2.Given a list
#
# l = [1, 1, 1, 2, 3, 3, 4, 5]
#
# new = []
#
# for i in l:
#     if i not in new:
#         new.append(i)
#
# print(new)
# # remove duplicates without set()
# #
# # 3.Given two lists
# #
# # l1=[23,45,78,90,12,74]
# #l2=[45,89,23,56,34]
# #
#
# # print common elelments
#
# l1 = [23, 45, 78, 90, 12, 74]
# l2 = [45, 89, 23, 56, 34]
#
# for i in l1:
#     if i in l2:
#         print(i)



# l=[1,1,1,2,3,3,4,5]
# s=set(l)
# print(s)
# print("updated list",list(s))


#
# l=[1,1,1,2,3,3,4,5]
#
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
#remove duplicates without set()


# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# s1=set(l1)
# s2=set(l2)
# print("common elements",s1.intersection(s2))



## DICTIONARY  ##,.....................................
#
# d={'name':'Arun','age':23,'place':'ekm'}
# d['name']