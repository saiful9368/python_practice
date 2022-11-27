#tuples - store multiple items in a single variable
#non homogeneous
#ordered
#immutable/unchangeable
"""mytuple=(1,2,3,4,4)
print(len(mytuple))
tuple1=("car","bike","boat","jet")
print(tuple1[1])
tuple2=tuple1+("cycle",)
print(tuple2)
z=list(tuple1)
z.append("cycle")
print(tuple(z))
tuple1=(10,20,30,40,50)
x=list(tuple1)
x.reverse()
print(tuple(x))
tuple1=("saiful",)

print(tuple1)

tup=(1,2,3,4,5,6,["a","b","c","d","e"],7,8,"q")
print(tup[6][0:3])
tup[6][2]=9
print(tup)"""

tuple1=(10,20)
tuple2=(30,40)
tuple1,tuple2=tuple2,tuple1
print(tuple1,tuple2)