mylist = [5,7,2,3,7,8,2,3,3]
newdict={}
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=1
    while j<len(mylist):
        if key== mylist[j]:
            count+=1
    if count > 1:
        newdict[key]=count
    max=newdict
    print(max)