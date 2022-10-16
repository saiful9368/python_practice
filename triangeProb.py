a=int(input("1st side = "))
b=int(input("2nd side = "))
c=int(input("3rd side = "))
if a+b>c and b+c>a and c+a>b:
    print("triangle can be formed")
else:
    print("triangle can not be formed")