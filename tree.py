#by using linked list 
#by using array

'''class tree:
    def __init__(self,data):
        self.data=data
        self.data=data
        self.child=[]
    def __str__(self,level=0):

        ret=" " *level+str(self.data)+"\n"
        for ch in self.child:
            ret+=ch.__str__(level+1)
        return ret

    def addchild(self,object):
        self.child.append(object)
        print("Tree node added")

rootnode=tree("drinks")
hot=tree("hot")
cold=tree("cold")
tea=tree("tea")
coffee=tree("coffee")
Nonalcholic=tree("non alchoholic")
Alchoholic=tree("alchoholic")

rootnode.addchild(hot)
rootnode.addchild(cold)
hot.addchild(tea)
hot.addchild(coffee)
cold.addchild(Nonalcholic)
cold.addchild(Alchoholic)

print(rootnode)'''

