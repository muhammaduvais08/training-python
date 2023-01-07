# def sum( a, b, c ):
#     z = a + b + c
#     print(z)
    
# sum(10,20, 100)
# sum(100,20, 100)
# sum(10,1120, 100)

# def odd_even( n ):
#     if n%2 == 0 :
#         print("Number is even")
#     else:
#         print("Number is odd")
        
# odd_even(10)
# odd_even(13)


# def sum( a, b, c ):
#     z = a + b + c
#     return z
    
# s = sum(10,20, 100)
# # print(s)

# # print(sum(100,200, 300))
# s1 =  sum(100,200, 300)
# print(s1)

# s = "Hello World!"
# x1 = len(s)
# print(x1)

# def odd_even( n ):
#     if n%2 == 0 :
#         return True
#     else:
#         return False

# def odd_even( n ):
#     if n%2 == 0 :
#         return True
#     return False
    
    
# print(odd_even(11))

# def is_prime( n ) :
#     i = 2
#     flag = True
#     while i < n :
#         if n % i == 0 :
#             flag = False
#             break
#         i = i +1
#     return flag

# print(is_prime(22))

# def display_list( l ):
#     for x in l:
#         print(x)
        
# display_list([10, 20, 30, 40])


# def chai_lao( x = 1 ):
#     print(f"{x} Chai are here")

# chai_lao(2)

# def display( x , y , z =300 ):
#     print(f"x={x}")
#     print(f"y={y}")
#     print(f"z={z}")
    
# display( 10, 20)

# def display( x = 1000 , y= 200 , z = 100 ):
#     print(f"x={x}")
#     print(f"y={y}")
#     print(f"z={z}")
    
# display(  y = 2, x = 100, z = 200 )

# x = 10
# y = 20

# # z = x if x < y else y

# # def fu1( x , y ):
# #     return x + y

# z = lambda x, y : x + y

# print( z(x, y) )

# Varibale Scope


x = 100

# def display():
#     y = 50
#     print("in display function")
#     print(f"Y is {y}")

# def display():
#     x = 10
#     print("in display function")
#     print(f"x is {x}")
#     def display_inner():
#         print("in display inner function")
    
#     display_inner()

# def display():
#     global x 
#     x = 10
#     print("in display function")
#     print(f"x is {x}")
    
# def display2():
#     y = 10
#     print("in display function")
#     print(f"x is {x}")
    
    
# print(x)
# display()

# print(f"x is {x}")

# x = 1
# while x < 11:
#     print("test")
#     print("Test")
#     x += 7

# S  M  T  W  T  F  S

f = int(input("first Day of month"))
d = 30

l = 'SMTWTFS'

for x in l:
    print( x , end='  ')

print()

print('   '* (f-1), end='')

c = 1
r = f
while c <= d :
    s = str(c)
    print( s.ljust(3), end='' )
    c = c + 1
    if r % 7 == 0 :
        print()
        r = 1
    else:
        r = r + 1
     



