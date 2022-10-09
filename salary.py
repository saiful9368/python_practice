'''print("employee bonus if there service is more then five years")
a=int(input("YEARS OF WORKING = "))
if a>=5:
    Current_salary=int(input("Current salary = "))
    bonus=Current_salary +1000
    print("net salary= ",bonus)
else:
    print("you are not eligible for bonus")'''
a=int(input("YEARS OF WORKING = "))
Csalary=float(input("current salary = "))
if a>=10:
    bonus = Csalary*0.1
    print("total salary now = ",Csalary + bonus)
if a>=6 and a<10:
    bonus = Csalary*0.08
    print("total salary now = ",Csalary + bonus)
if a<6 and a>0:
    bonus = Csalary*0.05
    print("total salary now = ",Csalary + bonus)
else :
    print(Csalary)