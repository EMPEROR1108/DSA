# Single level inheritance

'''class College:      # parent class
    def college_name(self):      # member function of college
        print("Modern College")


class Student(College):      # child class
    def student_info(self):      # member function
        print("Name: Prashant Jha")
        print("Branch: Mechanical")


obj = Student()      # object create child class
obj.college_name()
obj.student_info()'''


# Multilevel Inheritance

# First Class
class College:

    # First Level Method
    def college_name(self):
        print("Modern College of Engineering")


# Second Class
'''class Student(College):

    # Second Level Method
    def student_info(self):
        print("Name: Prashant Jha")
        print("Branch: Mechanical")


# Child Class
class Exam(Student):

    def subject(self):
        print("Subject1: Design")
        print("Subject2: Math")
        print("Subject3: C-Language")


# Object Creation
obj = Exam()

# Calling Methods
obj.college_name()
obj.student_info()
obj.subject()'''

# Multiple Inheritance Example

# Parent class - 1
class SubMarks:

    def __init__(self):
        self.math = int(input("Enter paper marks of math : "))
        self.DE = int(input("Enter paper marks of design engineering : "))
        self.c = int(input("Enter paper marks of c language : "))
        self.english = int(input("Enter paper marks of english : "))


# Parent class - 2
class PractMarks:

    def __init__(self):
        self.cpract = int(input("Enter practical marks of c language : "))


# Child class
class Result(SubMarks, PractMarks):

    def __init__(self):
        SubMarks.__init__(self)
        PractMarks.__init__(self)

    # if student pass in both subject and practical paper then pass
    def total(self):

        if (self.math >= 40 and self.DE >= 40 and
            self.c >= 40 and self.english >= 40 and
            self.cpract >= 20):

            print("Pass")

        else:
            print("Fail")


# Object creation
obj = Result()
obj.total()