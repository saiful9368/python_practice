print("***********CALCULATOR**********************")
def add(a,b):
    return a+b
def sub(a,b):
    return (a-b)
def multi(a,b):
    return (a*b)
def div(a,b):
    return(a/b)
def pow(a,b):
    return(a**b)

num1=int(input("num1-: "))
num2=int(input("num2-: "))

print("select the operater")
print("for addition  -: +")
print("for subtraction -: -")
print("for multiplication -: *")
print("for division -: /")
print("for power -: **")

chose=input("select operator  ")
if chose=="+":
    print(add(num1,num2))
elif chose=="-":
    print(sub(num1,num2))
elif chose=="*":
    print(multi(num1,num2))
elif chose=="/":
    print(div(num1,num2))
elif chose=="**":
    print(pow(num1,num2))
else:
    print("use correct input")
