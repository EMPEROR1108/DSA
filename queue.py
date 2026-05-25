'''
1.enque
2.dequeue
3.display queue
4.isEmpty()
5.isfull()
6.Delete
7.peek
'''
import sys
class Queue:
    def __init__(self,size):
        self.myQueue=[]#creating stack
        self.QueueSize=size #stack size defined

    def isFull(self):
        if len(self.myQueue)== size:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            print("queue is full")
        else:
             self.myQueue.append(value)
    
    def display(self):
        print(self.myQueue)
    
    def isEmpty(self):
        if self.myQueue ==[]:
            return True
        else:
            return  False
        
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            self.myQueue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.myQueue[0])
    
    def deleteQueue(self):
        self.myQueue=None


    

size=int(input("Enter the size of Queue: "))
obj =Queue(size)
print("Queue has Created: ")
while True:
    print("1.Enqueue Operation: ")
    print("2.Display Queue: ")
    print("3.Delete Operation: ")
    print("4.Peek operation: ")
    print("5.Delete Queue: ")
    print("6.Exit: ")
    choice=int(input("Enter your Choice: "))
    if choice ==1:
        value=int(input("Enter value to enqueue in queue: "))
        obj.enqueue(value)
    elif choice ==2:
        obj.display()
    elif choice==3:
        obj.dequeue()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.deleteQueue()
    elif choice == 6:
        sys.exit()