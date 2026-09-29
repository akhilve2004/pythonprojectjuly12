# class Person:
#     def __init__(self):
#
#         self.name=n
#         self.age=a
#
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person("arun",23)
# p2=Person("amal",24)
#
#
# p1.show()
# p2.show()


# define a class named student with attributes rollno,name,mark1,mark2,mark3 and method display()to display roll no and total mark of a student create 2 student object and call the methods



class Student:
    def __init__(self):
        self.rollno=int(input("enter roll number"))
        self.name=input("enter name")
        self.mark1=int(input("enter the mark1"))
        self.mark2 = int(input("enter the mark2"))
        self.mark3 = int(input("enter the mark3"))

    def display(self):
        print("Roll number",self.rollno)
        print()