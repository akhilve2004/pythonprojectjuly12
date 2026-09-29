class Category:
    def __init__(self):
        self.category_name=input("Enter category")

    def show_catergory(self):
        print("Category name",self.category_name)

class Product(Category):
    def __init__(self):
        super().__init__()
        self.product_name=input("Enter product name")
        self.price=int(input("Enter price"))
        self