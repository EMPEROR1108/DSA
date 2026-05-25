#input=vaibhav*is*a*good*programmer
#output=****vaibhavisagoodprogrammer
'''input_string = input("enter the string:")
output_string = ""
for char in input_string:
    if char.isalpha():
        output_string += char
    else:
        output_string = "*" + output_string
print(output_string)'''

name = "vaibhav*is*a*good*programmer"
newname = ""
val = ""
for i in  name:
    if i !='*':
        newname += i
    else:
        val+=i
print(newname)
print(str(val+newname))     
