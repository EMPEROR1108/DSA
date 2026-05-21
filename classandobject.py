# class Name:
#     age = 30
#     def display(self):#method (to access cureent method of class)
#        print("HELLO WORLD")
'''constructor'''
# obj = Name()
# print(obj.age)
# obj.display()
# class message:
#     def __init__(self):
#        print(" i am constructor")
    
#     def shows(self):
#         print("class program")

# obj = message()
# obj.shows()
# obj2=message()

'''parameterized constructor'''
class StudentInfo:
    def __init__(self,name,age,roll_no):
        self.Name = name
        self.Age = age
        self.RollNo = roll_no
    def displayStudentInfo(self):
        print("Name=", self.Name)
        print("Age=",self.Age)       

studentobject = StudentInfo("vaibhav",34,101)
studentobject.displayStudentInfo()

