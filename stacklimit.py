import sys
class Stack:
    def __init__(self,size):
        self.mystack=[]
        self.stackSize=size

    def isFull(self):
        if len(self.mystack)==self.stackSize:
            return True
        else:
            False

    def push(self,value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.mystack.append(value)
            print("Element Push")

    def display(self):
        print(self.mystack)
    
    def isEmpty(self):
        if self.mystack == []:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.mystack.pop())
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.mystack[-1])
    def delete(self):
        self.mystack=None

size=int(input("Enter the size of stack: "))
obj =Stack(size)
print("stack has Created: ")
while True:
    print("1.Push Operation: ")
    print("2.Display Stack: ")
    print("3.Pop Operation: ")
    print("4.Peek operation: ")
    print("5.Delete operation: ")
    print("7.Exit: ")
    choice=int(input("Enter your Choice: "))
    if choice ==1:
        value=int(input("Enter value to push in stack: "))
        obj.push(value)
    elif choice ==2:
        obj.display()
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.delete()
    else:
        sys.exit()