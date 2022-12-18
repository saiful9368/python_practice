"""class A:
    def method1(self):
        print("This is method 1")
class B(A):
    def method2(self):
        print("this is method 2")
class C(B):
    def method3(self):
        print("this is method 3")




object1=A()
object2=B()
object3=C()
object3.method1()"""
#multiple asking in one class
class A:
    def method1(self):
        print("This is method 1")
class B():
    def method2(self):
        print("this is method 2")
class C(B,A):
    def method3(self):
        print("this is method 3")




object1=A()
object2=B()
object3=C()
object3.method1()