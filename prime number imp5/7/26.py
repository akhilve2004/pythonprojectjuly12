#check whether a number is prime or not
#6-->1,2,3,6
#8-->1,2,4,8
#5-->1,5
#7-->1,7
num=int(input("enter a number"))
if(num>1):  #if number is greater than 1
    for i in range(2,num):
        if(num%i==0):
            print("not prime ")
        break
    else:
        print("prime number")
else:   #if number is 1,0 or negative
    print("number is neither prime or composite")