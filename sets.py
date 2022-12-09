#set -store multiple values in single variable
#unordered

mySet={"car","boat","train","b"}
#if "boat" in mySet:
#    print("boat")

mySet.add("cycle")
mySet2={1,2,3}
mySet.update(mySet2)
#print(mySet)
myset3={4,5,2,6,7}
output=myset3.intersection(mySet2)
output1=myset3.symmetric_difference(mySet2)
print(output)


#unchangeable/immutable
#duplicate not allowed
#non homogeneus
"""x=""
tuple1=("H","e","l","l","o")
for i in tuple1:
    x=x+i
print(x)

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n /= 5
    return s
n=int(input())
print(to_base_5(n))"""
