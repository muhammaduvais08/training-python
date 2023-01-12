# # Object Oriented Progarmming 

# class Person:
#     age = 23
#     weight = 70
#     name = "Tahseen"
    
#     def displayName():
#         print("Hello Name")
        
# Person.displayName()

# class Person:
#     def displayName( self , x ):
#         print("Hello ", self.name)
#         print("x=", x)
    
#     def displayAge( self ):
#         print("You age  ", self.age)
    
# p1 = Person()
# p1.name = "Amaan"
# p1.first_name = 22

# # print(p1.name)

# p2 = Person()
# p2.name = "Imran"
# p2.age = 20
# print(p2.name)
# print(p2.age)

# p2.displayName( 1000 )
# p1.displayAge()

class Person:
    
    def __init__( self , name, age ):
        print("In Init")
        self.name = name
        self.age = age
    
    def displayName( self , x ):
        print("Hello ", self.name)
        print("x=", x)
    
    def displayAge( self ):
        print("You age  ", self.age)
    
p1 = Person('Amaan', 21)

print(p1.name)

p2 = Person('Anas', 22)

# print(p2.name)
# print(p2.age)

p2.displayName( 1000 )
# p1.displayAge()