#wap to print row wise maximum element 
#[[100,198,333,323],
# [122,232,221,111],    
# [223,565,245,764]]
'''matrix = [[100,198,333,323],
          [122,232,221,111],    
            [223,565,245,764]]
for row in matrix:
    max = row[0]
    for element in row:
        if element > max:
            max = element
    print(max)'''
mylist = [[100,198,333,323],
          [122,232,221,111],
            [223,565,245,764]]
newlist = []
for i in range(3):
    j=0
    max = mylist[i][j]
    for j in range(4):
        c_max = mylist[i][j]
        if c_max > max:
            max = c_max
    newlist.append(max)
print(newlist)