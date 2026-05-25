#finding  vovels and length
v=['a','e','i','o','u']
w=input(("enter  the word where we will search the vovels:"))
found=[]
for i in w:
    if i in v:
        found.append(i)
print('found vovels=',found)
print('unique vovels',len(found),'from the given word=',w)