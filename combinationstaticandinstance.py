class Collage:
    collagename="modern collage"
    def __init__(self):
        self.studentname="vaibhav"
principal = Collage()
teacher = Collage()
accountant = Collage()
print("princapal=",principal.collagename,"   ",principal.studentname)
print("teacher=",teacher.collagename,"   ",teacher.studentname)
print("accountant=",accountant.collagename,"   ",accountant.studentname)
Collage.collagename="HBD"
principal.studentname="vaibhav aastha"
print("principal=",principal.collagename,"|",principal.studentname)
print("teacher=",teacher.collagename,"|",teacher.studentname)
print("accountant=",accountant.collagename,"|",accountant.studentname)
8