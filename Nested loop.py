#nested loop

# l=[10,20,30]
#
# for i in l:  #outer loop
#     for j in range(1,4):  #inner loop
#         print(i,end=" ")
#     print()
#......................................................................................................
# l=[1,2,3]
#
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#..........................................................
#1 2 3
#1 2 3
#1 2 3
# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

#.................................................................................................

# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print('outer loop itreation',i)
#     for j in i:
#         print(j,end=" ")
#     print()
#.......................................................................................
# n=['kelly','alan','jenny']
# for i in n:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#...............................................................................................
# n=[1,2,3]
# s=['what','when','why']
# for i in n:
#     print(i)
#     for j in s:
#         print(j,end=" ")
#     print()

#..........................................................................................

# d=[{'id':101,'name':'arun','age':25},{'id':102,'name':'amal','age':23},{'id':103,'name':'anu','age':24}]
#
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j,end=" ")
#     print()
#..................................................................................................
# #STAR PATTERN
#****                                     #i=1
#****                                          ****
#****                                      #i=2
# for i in range (1,4):  #row                     ****
#     for j in range(1,5): #column                  #i=3
#         print('*',end=" ")                   ****
#     print()
# ..................................................................................................:
   #*
   #**                                            #i=1
   #***                                                #*
   #****                                            #i=2
# for i in range(1,5):                                    #**
#     for j in range(1,i+1):                          #i=3
#         print('*',end=" ")                               #***
#     print()
#.............................................................................................................

#2 2 2 2
#4 4 4 4
#6 6 6 6
#8 8 8 8
# for i in range(2,9):
#     if i%2==0:
#         for j in range(1,5):
#             print(i,end=" ")
#     print()
#.......................................................................................................
#55555
#4444
#333
#22
#1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#       print(i,end=" ")
#     print()
#...............................................................................................
#****
#***
#**
#*
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#....................................................................................................
# 1111
# 2222
# 3333
# 4444
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#...................................................................................................
# 1000
# 0200
# 0030
# 0004
# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(i,end=" ")
#         else:
#             print(0,end=" ")
#     print()
#......................................................................................................
# 1
# 10
# 101
# 1010
# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2==0):
#             print(0,end=" ")
#         else:
#             print(1,end=" ")
#     print()
#.............................................................................................................
#REVISION.........
# *
# ***
# *****
# *******
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# **
# ****
# ******
# ********
# for i in range(2,9,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#...............................................................................................
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
#........................................................................................
# 1
# 4 9
# 16 25 36
# 49 64 81 100

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
#         k=k+1
#     print()
#......................................................................................................

# 1
# 3 5
# 7 9 11
# 13 15 17 19
#
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()
#..............................................................................................................
# A
# B C
# D E F
# G H I J
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
#...............................................................................................................
 # A
 # B B
 # C C C
 # D D D D
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()
#.............................................................................................
# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
#.................................................................................................

l=[23,65,42,80,56,41]
#print all even numbers
# for i in l:
#     if i%2==0:
#         print(i,end=" ")
#.......................................................................................................
#print all prime numbers
# for i in l:
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)
#....................................................................................................
#print all prime numbers in the range(1,100)
# for i in range(1,101):
#     if(i>1):
#
#         for j in range(2,i):
#             if(i%j==0):
#                 break
#         else:
#             print(i,end=" ")
#..................................................................................
#print all armstrong number in the range(100,1000)
# for i in range(100,1000):
#     s=str(i)
#     l=len(s)
#     sum=0
#     for j in s:
#         sum=sum+int(j)**l
#     if(sum==i):
#         print(i)


#...................................................................................

#SPACE PATTERN .........
# k=3*2
# for i in range(1,5):
#     #extra loop for adding space
#         for p in range(1,k+1):
#             print(end=" ")
#          #loop for printing stars
#         for j in range(1,i+1):
#             print('*',end=" ")
#         k=k-2
#         print()

#PYRAMID......................................
# k=3*2
# for i in range(1,5):
#     #extra loop for adding space
#         for p in range(1,k+1):
#             print(end=" ")
#          #loop for printing stars
#         for j in range(1,i+1):
#             print('*',end="   ")
#         k=k-2
#         print()
# ................................................................................
# for i in range(1,5):                                    #**
#     for j in range(1,i+1):                          #i=3
#         print('*',end=" ")                               #***
#     print()
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#......................................................................................................
# k=3*2
# for i in range(1,5):
#     #extra loop for adding space
#         for p in range(1,k+1):
#             print(end=" ")
#          #loop for printing stars
#         for j in range(1,i+1):
#             print('*',end=" ")
#         k=k-2
#         print()
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#.......................................................................................................

# k=3*2
# for i in range(1,5):
#     #extra loop for adding space
#         for p in range(1,k+1):
#             print(end=" ")
#          #loop for printing stars
#         for j in range(1,i+1):
#             print('*',end="   ")
#         k=k-2
#         print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end="   ")
#     k=k+2
#     print()

#........................................................................
# E
# DD
# CCC
# BBBB
# AAAAA
# n=ord('E')
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(n), end=" ")
#     n=n-1
#     print()
#................................................................
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
# #................................................
# for i in range(5,0,-1):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print()










