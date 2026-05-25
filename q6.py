#wap to access each character of string in forward and backward direction by using while loop
#i/p= "learning python is very easy"

s="learning python is very easy"
n=len(s)
i=0
print("forward direction")
while i<n:
    print(s[i],end= ' ')
    i+=1
print("backward direction")
i=1
while i>=-n:
    print(s[i],end=' ')
    i=i-1
