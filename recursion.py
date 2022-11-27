'''import sys
print(sys.getrecursionlimit())
def hello():
    print("hello world")
    hello()'''
#factorial number
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

x=int(input())
num=fact(x)
print(num)
'''
'''def square(x):
    return x**2

y=int(input())
p=square(y)
print(p)

def something(a):
    return a*a

x=lambda a:a*a
num=x(5)
print(num)


x=lambda a,b: a*b
num=x(5,10)
print(num)'''

def name(x):
    return lambda a:a+x

num=name(10)
print(num(5))