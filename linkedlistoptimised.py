import sys 
class Node:
    def __init__(self,data):
         self.data=data
         self.next=None
class linkedlist:
     def __init__(self):
        self.head=None
        self.tail=None
     def addNode(self,value):
         self.node=Node(value)
         if self.head is None:
             self.head=self.node
             self.tail=self.node
         else:
             self.tail.next=self.node
             self.tail=self.node
     def display(self):
        while self.head!=None:
            print(self.head.data,"|","-->",end=' ')
            self.head=self.head.next

     def addnodebig(self,value):
         print("Add node beginning:")
         self.node=Node(value)
         if self.head is None:
             self.head=self.node
             self.tail=self.node
         else:
             self.node.next=self.head
             self.head=self.node

     def addNodeBetween(self, index, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node

        elif index == 0:
            node.next = self.head
            self.head = node

        else:
            temp = self.head

        for i in range(index - 1):
            temp = temp.next

        node.next = temp.next
        temp.next = node
         

if __name__=="__main__":
    object=linkedlist()
    while True:
        print('1.Add node linkedlist:')
        print('2.Add node in beginning:')
        print('3.Add node in between:')
        print('4.Add node end:')
        print('5.Display linked list:')
        print('6.Exit')
        ch=int(input('enter your choice:'))
        if ch==1:
            value=int(input('enter value for node:'))
            object.addNode(value)
            print('Node added successfully in single linkedlist')
        elif ch==2:
            value=int(input('enter value for node:'))
            object.addnodebig(value)

        elif ch==5:
            object.display()

        elif ch==3:
             value=int(input('enter value for node:'))
             key=int(input("enter key after which to insert:"))
             object.addNodeBetween1
             (value,key)

        elif ch==6:
            sys.exit()  

            