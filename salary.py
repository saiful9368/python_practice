print("employee bonus if there service is more then five years")
a=int(input("YEARS OF WORKING = "))
if a>=5:
    Current_salary=int(input("Current salary = "))
    bonus=Current_salary +1000
    print("net salary= ",bonus)
else:
    print("you are not eligible for bonus") 