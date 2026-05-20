#binary search is faster than linear sarch(not all index are visited)
def binarysearch(array,target):
    low =0
    high=len(array)-1
    while low <= high:
        mid=(low+high)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            low= mid+1
        else:
            high=mid-1
            return -1
array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44]
target = 72
result=binarysearch(array,target)
if result == -1:
    print("element not found")
else:
    print("elemt found at",result)    
