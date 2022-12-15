# i = 1
# while i <= 10 :
#     if ( i ==  6 ):
#         break
#     print("i=", i)
#     i = i + 1
# else:
#     print("This is end of while")

# Prime number

# n =  int(input("Please enter any number: "))


# flag = True

# for i in range(2, n ) :    
#     if n % i == 0 :
#         flag = False
#         break
    
# if flag == True :
#     print("Number is prime")
# else:
#     print("Number is not a prime number")

# sum = 0 
# while True : 
#     n = input("Please enter any number or enter N to exit: ")
#     if n == 'N':
#         break
#     n = int(n)
#     if n % 2 == 0:
#         continue 
#     sum = sum + n

# print(sum)

# for i in range(1, 10):
#     if i == 5 :
#         continue
#     print("i= ", i)

# i = 1
# while i <= 10 :
#     print("in while i=", i)
#     if( i == 5 ):
#         i = i + 1
#         continue
    
#     print("i=", i)
#     i = i + 1

#find the calculator
s = 0 
while True :
    o = input("Enter +, -,  *, / or enter any thing else to exit")
    if o not in '+-*/':
        break
    
    n =  int(input("Eneter any number"))
    if o == '+':
        s = s + n
    elif o == '-':
        s = s - n
    elif o == '*':
        s = s * n
    elif o == '/':
        s = s / n
    
    print("s=",s)    

print("s=",s)




    
