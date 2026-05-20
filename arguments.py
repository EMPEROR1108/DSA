# def arithmatic(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum,sub,div,mul
# result = arithmatic(5,5)
# print("arithmatic = ", result)

# def credential(username,password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credenials")
# credential(username="admin",password="admin")        

# def cityname(city="pune"):
#     print(city)
# cityname("nagpur")
# cityname("mumbai")
# cityname()

#variable length argument/ variable number of argument 

# def cityname(name):
#     print(name)
# cityname("nagpur","delhi","mumbai","pune")    

import sys  
def add():
    a= int(input("enter value of a:"))
    b= int(input("enter value of b:"))
    print(a+b)
def sub():
    a= int(input("enter value of a:"))
    b= int(input("enter value of b:"))
    print(a-b)    
def mul():
    a= int(input("enter value of a:"))
    b= int(input("enter value of b:"))
    print(a*b)
def div():
    a= int(input("enter value of a:"))
    b= int(input("enter value of b:"))
    print(a/b)    

while True:
       print("1.addition")      
       print("2.substraction")        
       print("3.multiplication")        
       print("4.division")
       choice = int(input("enter your choice:"))
if choice == 1:
        add()
elif choice ==2:
        sub()
elif choice ==3:
        mul()
elif choice ==4:
       div()  
elif choice ==5:
      sys.exit()             
