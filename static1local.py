# instant variable
# class NEW:
#     def __init__(self):
#         self.a=10
# obj1 = NEW()
# obj2 = NEW()
# obj3 = NEW()
# obj1.a = 20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# static variable

class New:
    a=10
    def __init__(self):
        self.name="vaibhav"
obj1 = New()
obj2 = New()
obj3 = New()
New.a = 50
print(obj1.a)
print(obj2.a)
print(obj3.a)

