# class Person:
#
#     def __init__(self,n,a):    #__init__used to create and initialize
#                             #object attributes/properties
#         self.name=n
#         self.age=a
#
#     def show(self):     #self represents current object
#         print(self.name,self.age)
#
#         #static input
#
# p1=Person("arun",23)  #creates object of class person
#                              #it will call __init__() automatically
#
# p2=Person("amal",24)
#
# p1.show()
#
# p2.show()




# define a class named employee with attributes empid,name,age,place,salary,designation and methods getsalary()and showpersonaldetails()
# create an employee object and call the methods

class Employee:

    def __init__(self):
        print("enter employee details")

        self.empid=int(input("enter the ID"))
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.place=input("enter place")
        self.salary=int(input("enter salary"))
        self.designation=input("enter salary")

    def getsalary(self):
        print("salary",self.salary)

    def showpersonaldetails(self):



