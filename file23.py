# # For loop
# name = "Python Programming"

# for x in name :
#     print(x)
#     # print("For")
    
# print("End")

# name = "Python Programming"

# for x in name :
#     if x not in 'aiepou':
#         print(x)
    
# print("End")

# for i in range(1, 11):
#     print(i)

# for i in range(1, 50, 5):
#     print(i)
# sum = 0
# for i in range(1, 11):
#     sum = sum + i

# print(sum)
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

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end = ' ')
#     print()

# for i in range(1, 10):
#     pass

  
#      *
#    *   *
#   * * * *
#  *       *
# *         *


# for i in range(1, 6):
#     if i == 1: 
#         print( '*'. center(11))
#     elif i == 2: 
#         print( '*   *'. center(11))
#     elif i == 3: 
#         print( '* * * *'. center(11))
#     elif i == 4: 
#         print( '*       *'. center(11))
#     elif i == 5: 
#         print( '*         *'. center(11))

 
#      *
#    *   *
#   * * * *
#  *       *
# *         *

# * * * 
# *   *
# * * *
# *   *
# * * *

# 0, 3,5,  7, 9

h = 5
c= h*2+1
center_pos = h//2 + 1
for i in range(1, h+1):
    if i == 1 :
        print( '*'. center(c) )
    elif i == center_pos:
        print( ('* '*(center_pos+1)). center(c) )
    else:    
        print( ('*'+' '*(2*i-1) +'*').center(c) )


# *   *