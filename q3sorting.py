mylist = [5,7,8,3,7,8,9,2,3,2]
newlist=[]

for i in range(len(mylist)): #i=1
    count=0
    key=mylist[i]#key=7
    j=i+1
    while j<len(mylist):
        if key == mylist[j]: #7 == 3
            newlist.append(key)
        j=j+1
print(len(newlist))