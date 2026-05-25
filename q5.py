#wap to accept student name and marks from the keyboard and create a dictionary. also display studdent marks by taking student name
n=int(input("enter number of student:"))
d={}
for i in range(n):
    name=input("enter student name:")
    marks=input("enter marks of student:")
    d[name]=marks
while True:
    name=input(("enter student name to get marks:"))
    marks=d.get(name,-1)
    if marks== -1:
        print("student not found")
    else:
        print("the marks of",name ,"are",marks)
    optional=input("do you want to find another student marks[yes|no]")
    if option=="no":
        break
    print("thanks for using our application") 