#list

marks = [ 90, 80, 95, 88, 91 ] 

# print(marks)
print( type(marks))

# names = [ 'Waris', 22, 55.90, True ]

names = [ 'Waris', 22, 55.90, True, [ 90, 80, 95, 88, 91 ], 'Arwaz', 25  ]

# print(names[3])

# print(names)

# print(names[-2])

# print( names[2:5])

# print( len(names)) 


# marks1 = [101, 102, 100, 99, 98] 

marks1 =  list( (101, 102, 100, 99, 98) )

# print(marks1)
# print( type(marks1) )

# print( 'Amaan' in names)

# for x in marks :
#     print(x)

# i = 0
# while i < len(marks) :
#     print( marks[i] )
#     i = i + 1
    
marks = [ 90, 80, 95, 88, 91 ] 
max = marks[0]
for x in marks:
    if x > max  :
        max = x

print(max)
