# # #Account class
# #
# # class Account:
# #     def __init__(self):
# #         self.acctname=input("Enter account name")
# #         self.acctnumber=int(input("Enter the account number"))
# #         self.balance=int(input("Enter the balance"))
# #
# #     def showbalance(self):
# #         print("Current Balance",self.balance)
# #
# #     def withdraww(self):
# #         amount=int(input("Enter the amount"))
# #
# #         if(amount>self.balance):
# #             print("insufficient balance")
# #         else:
# #
# #             self.balance=self.balance-amount
# #
# #             self.showbalance()
# #
# #     def deposit(self):
# #         amount=int(input("Enter the amount"))
# #         self.balance=self.balance + amount
# #
# #         self.showbalance()
# #
# # a=Account()
# #
# # a.withdraw()
# #
# # a.deposit()
#
#
#
#
#
# #
# # l=[10,20,30]
# # for i in l:
# #     print(i)
#
#
#
# # l=["red","green","blue"]
# # for i in l:
# #     print(i)
#
#
# l=[a1,a2]
# for i in l:
#     #print(i.acctnumber,i.acctname,i.balace)
#     if(i.acctnumber==123):
#      i.showbalace()


# write a menu driven code for bank operations
#     using class and list
#     1 create  a new account
#     2 withdraw
#     3 deposit
#     4 showbalance
#     5 exit




#'
# Account class253

class Account:
    def __init__(self):
        self.acctname=input("Enter account name")
        self.acctnumber=int(input("Enter the account number"))
        self.balance=int(input("Enter the balance"))

    def showbalance(self):
        print("Current Balance",self.balance)

    def withdraww(self):
        amount=int(input("Enter the amount"))

        if(amount>self.balance):
            print("insufficient balance")
        else:

            self.balance=self.balance-amount

            self.showbalance()

    def deposit(self):
        amount=int(input("Enter the amount"))
        self.balance=self.balance + amount

        self.showbalance()