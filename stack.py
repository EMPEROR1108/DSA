# import sys
# class Stack:
#     def __init__(self):
#         self.mystack=[]

#     def push(self,value):
#         self.mystack.append(value)
#         print("Element Push")

#     def display(self):
#         print(self.mystack)

# obj =Stack()
# print("stack has Created: ")
# while True:
#     print("1.Push Operation: ")
#     print("2. enter value to put in stack:")
#     choice=int(input("Enter your Choice: "))
#     if choice ==1:
#         value=int(input("Enter value to push in stack: "))
#         obj.push(value)
#     elif choice ==2:
#         obj.display()
#     else:
#         sys.exit()
    

#pop method(remove) #pick(remove nhi krta )
import sys
class stack:
    def __init__(self):
        self.mystack=[]
    def push(self,value):
        self.mystack.append(value)
        print("element push")
    def display(self):
        print(self.mystack)
    def isEmpty(self):
        if self.mystack==[]:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self,self.mystack.pop())
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.mystack[-1])
    def delete(self):
        self.mystack=None

obj=stack()
print("stack has created")
while True:
   
    print("1.push operation:")
    print("2.display stack:")
    print("3.pop stack:")
    print("4. peek ")
    print("5.delete operation")

    print("7.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        value=int(input("enter value to push in stack:"))
        obj.push(value)
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.delete()
    else:
        sys.exit()