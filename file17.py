age = int(input("Please enter your age:"))

if age < 18 :
    print("Welcome")
    print("You are a teen ager")
    s = input("Are you a student Y/N:")
    
    if s == 'Y' :
        print("Very Good. Great Job keep learning")
    else :
        print("You should join any course")    
    
    print("End of Teen ager")
elif age < 35 :
    print("Welcome")
    print("You are a adult")
elif age < 55 :
    print("Welcome")
    print("You are a old man")
else:
    print("Welcome")
    print("You are a very old")
    
    
print("Exit")