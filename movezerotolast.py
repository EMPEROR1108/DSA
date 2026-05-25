    # i/p=[0,1,4,0,2,5]
    # o/p=[1,4,2,5,0,0]
mylist=[0,1,4,0,2,5]
print("original list:",mylist)
newlist=[]
for i in mylist:
    if i!=0:
        newlist.append(i)
for i in mylist:
    if i==0:
        newlist.append(i)
print("list after moving zeros to the end:", newlist)