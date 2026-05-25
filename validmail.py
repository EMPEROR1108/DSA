# import re
# s=input("Enter mail id: ")
# m=re.fullmatch("\w[a-zA-Z0-9_.]@gmail.com",s)
# if m!=None:
#     print("Valid E-mail Id")
# else:
#     print("Invalid E-mial ID")

'''valid mobile no'''
'''
import re
mo=input("Enter Moblie number:")
obj=re.fullmatch("[0-5]\d{9}",mo)
if obj!=None:
    print("Valid Number")
else:
    print("Invalid Number")
'''

#serch() function
'''import re
a=input("Enter string to perform match opertaion: ")
mtch=re.search(a,"python sss dynamic lannn")
print(mtch)
if mtch!=None:
    print(mtch.start()," ",mtch.end()," ",mtch.group())
else:
    print("there is no ,matching anywhere")'''

#findall()
'''import re
mtch=re.findall('[A-Z]',"abch3hdh5bk7ZQ%&*")
print(mtch)'''

#sub()
'''import re
obj=re.sub('[a-z]','*','2345 ABCS hbbs deff')
print(obj)'''

#subn()returns count of replacement
'''
import re 
obj = re.subn('[0-7]','@','ab3gd6nkKL7' )
print(obj)
print("the string is=",obj[0])
print("the number of replacement is=",obj[1])
'''
#wap to extract all mobile no
#input.txt where numbers are mixed with normal
'''import re 
f1=open("input.txt","r")
f2=open("output.txt","w")
#for line in f1:
# WAP to extract all mobile numbers from input.txt

import re

f1 = open("input.txt", "r")
f2 = open("output.txt", "w")

for line in f1:
    numbers = re.findall(r"[6-9]\d{9}", line)
    
    for num in numbers:
        f2.write(num + "\n")

print("Mobile numbers extracted successfully!")

f1.close()
f2.close()
'''


# Program to print the number of lines, words and characters present in the given file

import os, sys

fname = input("Enter file name: ")

if os.path.isfile(fname):
    print("File exists:", fname)
    f = open(fname, "r")
else:
    print("File does not exist", fname)
    sys.exit(0)

lcount = wcount = ccount = 0

for line in f:
    lcount = lcount + 1
    ccount = ccount + len(line)

    words = line.split()
    wcount = wcount + len(words)

print("The number of lines:", lcount)
print("The number of words:", wcount)
print("The number of characters:", ccount)