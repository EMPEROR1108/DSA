'''BINARY TREE'''


'''
FULL BINARY TREE
1.EACH NODE HAS EITHER 0 OR 2 CHILDREN
2. NO NODE HAS SINGLE CHILDREN'''

'''
COMPLETE BINARY TREE
1.ALL LEVELS EXPECT POSSIBLY THE LAST ARE COMPLETELY FIELD
2.NODES IN THE LAST LEVEL ARE FILLED FROM LEFT TO RIGHT'''

"""
PERFECT BINARY TREE
 1.ALL INTERNAL NODES ARE EXACTLY TWO NODES
 2 ALL LEAF NODES ARE AT SAME LEVEL"""

'''
BINARY SEARCH TREE
IT PEFORMS BETTER THAN BINARY TREE WHEN INSERTING AND DELETING NODES'''
class BSTNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild=None
        self.rightChild = None

def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")

def searchNode(rootNode, nodeValue):
    
    if rootNode.data == nodeValue:
        print("Value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild==nodeValue:
            print("Value found")
        else:
            searchNode(leftChild, nodeValue)
    else:
        if rootNode.rightChild==nodeValue:
            print("Value found")
        else:
            searchNode(rightChild, nodeValue)


newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
preOrderTraversal(newBST)
print()
inOrderTraversal(newBST)
print()
postOrderTraversal(newBST)