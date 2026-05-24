# def insertion(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while(j>=0) and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr
# n=[5,3,8,6,2]
# sortedarr=insertion(n)
# print(sortedarr)

# Selection Sort
arr1 = [20, 12, 10, 15, 2]

for i in range(len(arr1)):
    min_index = i
    j = i + 1

    while j < len(arr1):
        if arr1[j] < arr1[min_index]:
            min_index = j
        j += 1

    arr1[i], arr1[min_index] = arr1[min_index], arr1[i]
    print(arr1)

print("Sorted array:", arr1)