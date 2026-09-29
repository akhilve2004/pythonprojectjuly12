# create an abstract class shape










   @abstractmethod
   def get_area(self):
       pass

   @abstactmethod
   def get_perimeter(self):
       pass



#s=Shape()

class Rectangle(Shape):

    def __init__(self):
        self.length=int(input("enter length"))
        self.breadth=int(input("enter breadth"))

    def get_area(self):
        print("Area",self.length*self.breadth)
