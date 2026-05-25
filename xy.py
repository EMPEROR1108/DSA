# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# val=[2**i for i in range(1,6)]
# print(val)

# s=[i*i for i in range(1,11)]
# print(s)

# square={x:x*x for x in range(1,6)}
# print(square)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

# a,b=[int(x) for x in input("enter 2  number:").split()]
# print("product is:",a*b)

# a,b,c=[float(x)for x in input("enter 3 float number :").split(',')]
# print("the sum is :", a+b+c)

# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("this is not my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased everthing")

"""username = "admin"
password = "admin"
enter username
enter password"""

while True:
    username= input("enter username:")
    password= input("enter password:")
    if username =="admin" and password == "admin":
        print("login")
        break
    else:
        print("invalid")