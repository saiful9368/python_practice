"""def isEven(i):
    return i%2==0
list1=[3,2,8,16,11,34,17]

output=list(filter(isEven,list1))
print(output)"""

list1=[3,2,8,16,11,34,17]
output=list(filter(lambda i:i%2==0,list1))
output=list(filter(lambda i:i>15,list1))
print(output)
output2=map(lambda i:i**2,list1)
print(list(output2))