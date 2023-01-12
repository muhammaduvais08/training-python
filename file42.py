# class Person:
    
#     def __init__( self , name, age , s):
#         # print("In Init")
#         self.name = name
#         self.age = age
#         self.__salary = s
    
#     def displayName( self ):
#         print("Hello ", self.name)
#         print("Salary ", self.__salary)
#         self.__displayAge()
        
#     def __displayAge( self ):
#         print("You age  ", self.age)
    
#     def __str__( self ):
#         return "Hello"
    
# p1 = Person('Amaan', 21, 100000)
# # x = 100
# # print( type(x))
# # print(p1.__salary)
# # p1.displayName()
# # p1.__displayAge()

# print(p1)
# # class A:
# #     pass

class Desktop:
    def __init__(self, s , r) :
        self.screen = s
        self.ram = r
    
    def display( self ):
        print("In Desktop")
        print("Screen =",self.screen)
        print("Ram =",self.ram)
        
    def displayScreen(self):
        print("Screen =",self.screen)
    
    def displayRam(self):
        print("Ram =",self.ram)
        
    def off (self):
        print("Now system is off")
        
    def on(self):
        print("Now system is on")
        
        
# d1 = Desktop("14", 512)
# d1.displayDesktop()
# d1.displayScreen()
# d1.displayRam()
# d1.on()
# d1.off()

class Lapptop (  Desktop ):
    def __init__(self, s, r, b):
        super().__init__(s, r)
        self.baterry = b
    
    def webCamera(self):
        print("Camerea is on")
    
    def display( self, message ):
        print(message)
        print("In Desktop")
        print("Screen =",self.screen)
        print("Ram =",self.ram)
        print("baterry =",self.baterry)


l1  = Lapptop("14", 512, 5000)
# print(l1.screen)
l1. display()
# l1.webCamera()
# l1.on()
# l1.off()

        