marks = [ 
         [ 98, 67, 56, 57, 81  ],
         [ 81, 97, 72, 82, 62  ],
         [ 65, 57, 54, 71, 73  ],
         [ 62, 87, 81, 79, 95  ],
         [ 64, 85, 56, 80, 82  ]             
]

# print(marks[0][2])

# print(marks[1][4])
# max = marks[0][0]
# for x in marks :
#     for i in x:
#         print(i)

i  = 1
for m in marks :
    # print(x)
    sum = 0 
    for n in m:
        sum +=  n
    m.append(sum)
    i = i + 1
    
# print(marks)
        
        
# lst = [ 98, 67, 56, 57, 81, 82, 99, 102, 91, 90  ]
# even_list = [] 

# for x in lst:
#     # print(x)
#     if x % 2 == 0 :
#         even_list.append(x)

# print(even_list)

# x = 10
# y = 5
# if ( x < y ):
#     z = x 
# else: 
#     z = y

# z = x if x < y else y   

# print(z)      

# lst = []
# for x in 'Tahseen':
#     if x not in 'aieuo' :
#         lst.append(x)

# print(lst)

# newlist = [ expression for item in iterable if condition == True]
# a = 100
# lst = [ True for x in 'Tahseen' if True ]
# print(lst)

lst = [ 98, 67, 56, 57, 81, 82, 99, 102, 91, 90  ]
even_list = [ 'Arwaz' for x in lst if x % 2 == 0 ] 
print(even_list)