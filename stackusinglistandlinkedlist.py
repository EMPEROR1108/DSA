'''stackk using list
*easy to implement
*speed problem when it grows'''

'''stack using Linked list
*fast performance
*implementation is not easy'''

fruit={}  #{'Apple':1,'Banana':1,'apple':1}
def addone(index):
    if index in fruit:
        fruit[index] +=1
    else:
        fruit[index]=1
addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))