def arithmatic():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    sum = a+b
    sub = a-b
    div = a/b
    mul = a*b
    return sum,sub,div,mul
result = arithmatic()
print("arithmatic = ", result)
