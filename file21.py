# i = 0 
# while i < 11:
#   print(i)
#   i += 1
# else:
#     print("End of while")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# i = 1
# while i <= 5 :
#     j = 1 
#     while j <= i :
#         print(j, end = ' ')
#         j = j + 1
    
#     i = i + 1
#     print()

# *
# **
# ***
# ****
# *****

# i = 1
# while i <= 10 :
#     j = 1 
#     while j <= i :
#         print('*', end = ' ')
#         j = j + 1
    
#     i = i + 1
#     print()

# i = 1
# while i <= 5 :
#     print('*'*i, end = ' ')    
#     i = i + 1
#     print()

# i = 1
# sum = 0 
# while i <= 10 :
#     sum = sum + i
#     i = i + 1
    
# print(sum)

sum = 0
num  = 1
while  num!= 'N' :
    num =  input("Please enter any number or N to exit")
    if( num != 'N' ):
        num = int(num)
        sum = sum  + num
    
print(sum)