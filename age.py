a=int(input("enter the age of P1 = "))
b=int(input("enter the age of p2 = "))
c=int(input("enter the age of p3 = "))
if a>b and a>c:
    print("p1 is greatest and p3 is smallest")

if b>c and b>a:
    print("p2 is greatest and p1 is smallest")

if c>a and c>b:
    print("p3 is greatest and p2 is smallest")
