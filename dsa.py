# dsa is a way of organizing data on your computer that can be used effectively
#constatnt time
# array={1,2,3,4,5}
# array[0]
# o(n) liner time
# array={1,2,3,4,5}
# for element in array:
    # print(element) 

# o(logN) logarathmic time
# array={1,2,3,4,5}
# for index in range {0 ,  len(array),3}
    # print(array[index])

# def linearsearch(array, target):
#   for i in range(0,len(array)):
#     if array[i]==target:
#       return i
#     return -1
# array=[1,2,3,4,8,7,9]
# target=10
# result=linearsearch(array,target)
# if result==-1

city=input("enter city name:")
scity=city.strip()
if scity=="hydrabad":
    print("welcome to hyderabad")
elif scity=="pune":
    print("welcome to pune")
elif scity=="mumbai":
    print("welcome to mumbai")
else:
    print("welcome to india")      