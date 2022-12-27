# question = [
#     ['q1', 'option1', 'option2', 'option3', 'option4', 'c',1, 'c'  ] ,
#      ['q2', 'option1', 'option2', 'option3', 'option4', 'd', 0, 'a'  ]    ,
# ]

#Dictionary 

# city =   { 'name' : 'New Delhi', 'pop' : 2000000, 'area': 100000, 'cm':'Arvind', 'literacy' : 60.50, 
#             'dist_pop' : [100000, 200000, 150000, 30000]   
#         } 

# # print(city)

# # print( type(city) )

# # print(city['dist_pop'])

# # print( city.get('pop') )

# print( id (city['dist_pop']) )

# dist_pop = city['dist_pop']

# dist_pop[1] =  1500

# dist_pop = "Test"

# print( id (dist_pop) )
# # dist_pop[1] =  1500

# # dist_pop = [100000, 1500, 150000, 30000]
# # name = city['name']

# # name = "Mumbai"

# # print(name)

# print(city)

city = dict( { 'name' : 'New Delhi', 'pop' : 2000000, 'area': 100000, 'cm':'Arvind', 'literacy' : 60.50, 
            'dist_pop' : [100000, 200000, 150000, 30000]   
        }  )
# print(city)
# print(type(city.keys()))
# print(city.values())

# for x in city.keys():
#     print(x)
#     print(city[x])


# for x in city.values():
#     print(x)

# x = city.values()
# print(x)
# city['name'] = 'Pilibhit'
# print(city)
# print(x)

# print(city.items())

# for x in city.items():
#     # print(type(x))
#     print(x[0])
#     print(x[1])

# for x in city.items():
#    (key, value) =  x
#    print(value)


# for (key, value)  in city.items():
#    print(value)

# print(city)
# city['test'] = 1
# print(city)

# a = { 'a': 1, 'b': 2, 'c': 3}
# b = a
# print(a)
# print(b)
# a['d'] = 4

# print(a)
# print(b)
a = { 'a': 1, 'b': 2, 'c': 3}
b = a.copy()
print(a)
print(b)
a['d'] = 4

print(a)
print(b)
