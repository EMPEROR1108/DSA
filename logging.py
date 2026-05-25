try:
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("cant divide by zero")
except ValueError:
    print("Enter only integer value")
except:
    print("Error")
finally:
    print("im always executed")
# else:
#     print("Everything is okay")
# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

import logging
logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
try:
    a=int(input("enter first integer no")) 
    b=int(input("enter second integer no")) 
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is set up. Check 'newfile.txt' for log details.")