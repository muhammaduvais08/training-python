#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# i = 1
# while i <= 5 :
#     s = '* '*(2*i-1)
#     print(s.center(18))
#     i += 1

#9, 7, 5, 3 , 1 (Space)
#1, 3, 5, 7, 9 ( *)
# 10-(2*i-1)

# i = 1
# while i <= 5 :
#     print( ' '*(10-(2*i-1)), end = '')
#     print('* '*(2*i-1))
#     i += 1

#9, 7, 5, 3 , 1 (Space)
#1, 3, 5, 7, 9 ( *)

i = 1
while i <= 5 :
    j = 1
    while j <= (10-(2*i-1)) :
        print(' ', end='')
        j = j + 1
       
    k = 1
    while k <= (2*i-1) :
        k = k + 1 
        print('* ', end='')
    i += 1
    print( )