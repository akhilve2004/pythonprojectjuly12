#new={key:value for item in iterable if condition}

#eg given a list
l=[1,2,3,4]
#create a new dictionary where keys are numbers and values the sqare of each number
#out{1:1,2:4,3:9}
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#comprehension

# new={i:i**2 for i in l}
# print(new)
# new={i:i**3 for i in l}
# print(new)

#...................................................
#given a list
# l=[10,20,30,40]
# #create a new dictionary where keys are index and values are numbers itself
# #out{0:10,1:20,2:30}
# new={i:l[i] for i in range(0,len(l))}
# print (new)

#....................................................................
#given a string
s="python coding is easy and fun"
#create a new dictionary where keys are words and values are length of  easch word
# new={"python":6,"coding":6,"is":2,"easy":4,"and":3,"fun":3}
# for i in s:
#     print (i)
#

# for i in s.split():
#     print(i)
new={i:len(i) for i in s.split()}
print(new)