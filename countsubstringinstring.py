str=input("enter the string: ")
sub=input("enter the substring: ")
count=0
for i in range(len(str)):
    if str[i:i+len(sub)]==sub:
        count+=1
        print(count)