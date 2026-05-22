# # #listcollection datatype
# #mylist= ["prashant", "suman", "satyarth", 77, "pratik", 60 , 50 ,"vaibhav"]
# print(mylist)
# # print(type(mylist))
# # print(mylist[0])
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[-1])
# # print(mylist[2:5])
# # print(mylist[:5])
# # print(mylist[2:])
# # print(mylist[2:5:2])

# mylist[2]="rohit"
# print(mylist)

# if "prashant" in mylist:
#     print("prashant is present in the list")
# else:
#     print("prashant is not present in the list")

# mylist.append("janvi")
# mylist.append("moti")
# print(mylist)  
# mylist.insert(2,"satyarth")
# print(mylist)

# mylist.remove("satyarth")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)

# mylist= [['prashant','jha'],['85','90'],['440022','yyy']]
# print("example of multidimensional list:")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list2=[50,60,70,"prashant"]
# list2.clear()
# print(list2)

# name="prashant"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[44,22,77,0,9,88]
# mylist.sort(reverse=True)
# print(mylist)
mylist=[44,22,77,0,9,88]
newlist=mylist
print(id(mylist))
print(id(newlist))
