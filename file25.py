# Prime number

n =  int(input("Please enter any number: "))

i = 2

flag = True

while i < n :
    
    if n % i == 0 :
        flag = False
        break
    i = i +1
    
if flag == True :
    print("Number is prime")
else:
    print("Number is not a prime number")


    
