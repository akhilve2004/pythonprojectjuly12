# #inheritance
#
# class Parent:
#
#     def m1(self):
#         print("In Parent class method m1")
#
#     def m2(self):
#         print("In Parent class method m2")
#
# #p=Parent()
# #p.m1()
# #p.m2()
#
# class Child(Parent):
#     def m1(self):
#         super().m1()
#         print("in child class m1")
#     def m3(self):
#         print("in child class m3")
#
# c=Child()
#
# c.m1()
# c.m2()
# c.m3()





class Person:
    def __init__(self):
        self.name=input("Enter name")
        self.age=int(input("enter age"))
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=int(input("Enter roll number"))
        self.course=input("Enter course")
        self.mark=int(input("Enter mark"))
    def show(self):
        super().show()
        print(self.rollno,self.mark,self.course)

    def updatemark(self):
        self.mark=int(input("Enter new mark"))


s=Student()
s.show()
s.updatemark()