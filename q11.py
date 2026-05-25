#remove leading zeros from a list of integers
'''def remove_leading_Zeros(nums):
    for i in range (len(nums)):
        if nums[i] != 0:
            return nums[i:]
    return[]
print(remove_leading_Zeros([0,0,7,8,0]))'''

#find missing positive integer:
def first_missing_positive(nums):
    n = len(nums)

    # Place each number at its correct index: value -> index (value-1)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # swap nums[i] with nums[nums[i] - 1]
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # After placing, the first location where index != value is the answer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all correct positions filled, next positive is n+1
    return n + 1
print(first_missing_positive([3,4,-1,1]))
