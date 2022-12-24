# question = [
#     ['q1', 'option1', 'option2', 'option3', 'option4', 'c',1, 'c'  ] ,
#      ['q2', 'option1', 'option2', 'option3', 'option4', 'd', 0, 'a'  ]    ,
# ]

#Dictionary 

city =   { 'name' : 'New Delhi', 'pop' : 2000000, 'area': 100000, 'cm':'Arvind', 'literacy' : 60.50, 
            'dist_pop' : [100000, 200000, 150000, 30000]   
        } 

# print(city)

# print( type(city) )

# print(city['dist_pop'])

# print( city.get('pop') )

print( id (city['dist_pop']) )

dist_pop = city['dist_pop']

dist_pop[1] =  1500

dist_pop = "Test"

print( id (dist_pop) )
# dist_pop[1] =  1500

# dist_pop = [100000, 1500, 150000, 30000]
# name = city['name']

# name = "Mumbai"

# print(name)

print(city)