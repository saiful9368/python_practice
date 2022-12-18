# b=[1,2,4,5,6,6,7]
# print(len(b))

# def add(a,b,c =0):     #this called method overloading
#     return a+b+c
# print(add(1,2))
# print(add(1,2,3))

# class Rect:
#     def calculateArea(self,length=None,breadth=None):
#         if length!= None and breadth!= None:
#             return length*breadth
#         elif length!=None:
#          return length*length
#                                                 #this is over loading👈👈👈👈👈👈👈
# reactangle=Rect()
# print(reactangle.calculateArea(2,3))
# print(reactangle.calculateArea(4,3))

"""class Bird:
    def category(self):
        print("This is a Category of Bird")
    def fly(self):
        print("I can fly")
class sparrow(Bird):
    def sizeParameter(self):
        print("I am small in size")
class crow(Bird):
    pass
class ostrich(Bird):
    def fly(self):
        print("I cannot fly, sorry")
objb=Bird()
objsp=sparrow()
objcr=crow()
objos=ostrich()

objb.category()
objb.fly()
objsp.category()
objsp.fly()
objcr.category()
objcr.fly()
objos.category()
objos.fly()"""

class vhiecle:
    def stcap(self):
        print("Seating capacity is 4")
class car1(vhiecle):
    pass
class car2(vhiecle):
    pass
class bus(vhiecle):
    def stcap(self):
        print("Seating capacity is 40")

BMW=car1()
Audi=car2()
buss=bus()

BMW.stcap()
Audi.stcap()
buss.stcap()