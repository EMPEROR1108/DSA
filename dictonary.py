#

'''a=mydict[102]
print(a)'''

'''a=mydict[102]="bail"
print(a)'''

#for x in mydict:
 #   print(x)

# for x in mydict.values():
    # print(x)

'''for x,y in mydict.items():
    print(x,y)'''

#adding new key value pair
'''mydict["mobile"] = "1234567890"
print(mydict)'''

'''mydict.pop(101)
print(mydict)'''
#pop method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError. If the key is found, it removes the key-value pair from the dictionary and returns the value associated with that key.

'''a={(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])'''

'''a={'a':1,'b':2,'c':3}
print(a['a','b'])'''

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1] += 1
# sum = 0
# for k in arr:#k='1'
#     sum+= arr[k]
#     print (sum)

# my_dict={}
# my_dict[1] = 1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)
 
# my_dict={}
# my_dict[(1,2,4)]= 8
# my_dict[(4,2,1)] =10
# my_dict[(1,2)]=12
# sum = 0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)
# print(my_dict)
 
# box ={}
# jars ={}
# crates ={}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

#dict ={'c':97,'a':96, 'b':98}
#for _ in sorted (dict):
 #print(dict[_])

# rec = {"Name" : "python", "Age":"20", "Addr": "N","country":"usa" }
# id1=id(rec)
# del rec
# rec={"name": "python","Age":"20","Addr":"Nj","country":"usa"}
# id2=id(rec)
# print(id2)
# print(id1==id2)

#find the key with the  maximum  value in the dictonary
# my_dict={'a':50,'b':40,'c':70}
# max = max(my_dict.keys())
# print(max)
# min = min(my_dict.keys())
# print(min)

