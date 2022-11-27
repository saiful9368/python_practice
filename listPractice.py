"""
#list - it stores multiple items in a single variable
# non homogeneous
#ordered
#Changable / mutable
#allows duplicate values

#append() - add at the end of list
#insert() - insert item at particular index
#extend() - add elements from one list to another
#remove() - remove list element
#pop() - remove with specific index
#del and #clear
#sort() - sort the list in ascending order
# 
# 
# 
# 
# x=["red","red","black",22]
'''print(x[::-1])
x[0:2]="yellow","white","orange"
print(x)
x.insert(2,"indigo")
print(x)
x.append("blue")
#for remove specific index
print(x.pop())
print(x)
#for deleting whole list
#x.clear()
'''
for i in x:
    print(i)

i=0
while i<len(x): 
    print(x[i])
    i+=1
#one line programm
#[print(i) for i in x]"""
#cars=["TATA","NANO","ALTO","JEEP"]
"""newlist=[]
for i in cars:
    if "A" in i:
        newlist.append(i)
print(newlist)"""

#newlist=[x for x in cars if x == "TATA"]
#print(newlist)

#newlist=[x.lower() for x in cars]
#print(newlist)
"""numbers=[1,5,10,3,6,5]
new=[]
numbers.sort()
#print(numbers)
for i in numbers:
    z=i**2
    new.append(z)
print(new)"""
"""n=[1,2,3,4,5,2,6]
a=n.index(2)
print(a)
for i in n:
    if n[i] == 2:
        n[a]=200
        break
print(n)"""

'''num2=[1,4,6,2,10]
num1=num2.copy()
num3=list(num1)
print(num1,num3)'''

#concatination
x=["a","b","c"]
print(x+[1,12,23,4])
x.insert(2,3)
print(x)
x.extend("a")
print(x)
x.remove("a")
print(x)
#print(x.sort())
y=["saiful","ankit","aasim","sait"]
y.sort()
print(y)