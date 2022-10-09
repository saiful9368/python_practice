print("Temprature converter ")
print("F TO CELCIUS OR C TO F")
temp1=input("F or C= ")

if temp1=="F":
    F=float(input("temp in f = "))
    C=(F-32)*5/9
    print(C)

if temp1=="C":
    C=float(input("temp in c = "))
    F=1.8*C+32
    print(F)
else:
    error="plz ener in capital letters"
    print(error)