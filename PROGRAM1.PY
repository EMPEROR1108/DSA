# # 
# #why all fundamental data types are immutable in python?
# math=50
# chemistry=50
# phy=50
# print(id(math))
# print(id(chemistry))
# print(id(phy))

# print(2+2)
# print("2"+"2")
# a = int (input("enter first number : "))
# b = int (input("enter second number : "))
# print(a+b)

#int
# print(int(3.14))
# #print(int(10+5j))#error
# print(int(True))#1
# print(int(False))#0 
# #print(int("3.14"))#error
# print(int("10"))
# #print(int("vaibhav"))#error

 #float
# print(float(3))
# #print(float(10+5j))#error
# print(float(True))#1
# print(float(False))#0 
# print(float("3.14"))
# print(float("10"))
# #print(float("vaibhav"))#error

#complex
# print(complex(3.14))
#  #print(complex(10+5j))#error
# print(complex(True))#1
# print(complex(False))#0 
# print(complex("3.14"))#error
# print(complex("10"))
#  #print(complex("vaibhav"))#error    
# print(complex(3,-4))
# print(complex(True,False))

#boolean
# print(bool(3.14))
#  #print(complex(10+5j))#error
# print(bool(True))#1
# print(bool(False))#0 
# print(bool(1+2j))#error
# print(bool("10"))
# print(bool(0+0j))
# print(bool(-1))
#  #print(bool("vaibhav"))#error    
# #print(bool(3,-4))
# print(bool(""))

#simple if
# a= int (input("enter any single digit  : "))
# if a>0:
#     print("positive number")
# if a<0:
#     print("negative number")
# if a==0:
#     print("zero")    

#if else
#monday-friday- working day
#saturday-sunday- weekend
# day = input("enter the day : ")
# if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
#     print("working day")
# else:
#     print("weekend")

# per=65
# if per>=65:
#     print("grade A")
# elif per<=65 and per>=50:
#     print("grade B")
# else: 
#     print("fail")        

chr = ord(input("enter any character : "))
if chr>=65 and chr<=90:
    print("uppercase")
elif chr>=97 and chr<=122:
    print("lowercase")
elif chr>=48 and chr<=57:
    print("digit")   
else:
    print("not an alphabet")    