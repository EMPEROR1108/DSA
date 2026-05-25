# wap to accept three paper marks and calculate the total and percentage and chrck if he/she is passed in all subbject
# so print pass else print fail

# if percantage is greater than 65 and gender = "male" so he is eligible for placement else he is not eligible for placement  

first_paper = int(input("enter the marks of first paper : "))
second_paper = int(input("enter the marks of second paper : "))
third_paper = int(input("enter the marks of third paper : "))
print("total marks is : ", first_paper + second_paper + third_paper)
percentage = (first_paper + second_paper + third_paper) / 3
print("percentage is : ", percentage)
if first_paper >= 35 and second_paper >= 35 and third_paper >= 35:
    print("pass")
else:
    print("fail")

gender = input("enter the gender : ")

if percentage > 65 and gender == "male":
    print("he is eligible for placement")
else:
    print("he is not eligible for placement")   