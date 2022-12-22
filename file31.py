
items = []  
while True :
    option = int( input("Enter 1 to add \n 2 to Pop or \n 0 to exit") )
    if option == 0 :
        break
    elif option ==  1 :
        text =  input("Input item to add")
        items.append(text)        
    elif option ==  2:
        if len( items ) > 0 :
            t = items[0]
            print(f"Pop item is {t}")
            del items[0]
        else:
            print("Empty list")            
    else:
        print("Invalid Input")    
    
    print("New list is")
    print(items)
    
