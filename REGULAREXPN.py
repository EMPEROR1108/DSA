# import re   # module for performing all the regular expression based operations

# count = 0

# pattern = re.compile("python")   # string converts into bytecode

# matcher = pattern.finditer(
#     "A function in python is defined by a def statement. "
#     "The general syntax looks like this: "
#     "def function_name(parameter list): statements, i.e. the function body. "
#     "The parameter python list consists of none or more parameters."
# )

# for i in matcher:
#     count += 1
#     print(i.start(), "", i.end(), "", i.group())

# print("The number of occurrences:", count)


'''import re
count=0
matcher=re.finditer("Hi","HiHiHiHi")
for i in matcher:
    count+=1
    print(i.start(),"...",i.end(),"...",i.group())
print("The number of occurrences: ",count)'''

'''import re
obj=input("vaibhav : ")
objmatch=re.finditer(obj,"a7b @k9z")
for match in objmatch:
    print(match.start(),"...",match.end(),"...",match.group())'''

'''import re
a=input("Enter string to perform match operation: ")
mtch=re.match(a,"Python is very important language")
print(mtch)
if mtch!=None:
    print("Match found at Begining Level")
    print(mtch.start()," ",mtch.end())
else:
    print("There is no matching at begining level")'''

'''import re
a=input("Enter string to perform match operation: ")
mtch=re.match(a,"Pythonisvery")
print(mtch)
if mtch!=None:
    print("Match found ")
    print(mtch.start()," ",mtch.end())
else:
    print("full match not found")'''