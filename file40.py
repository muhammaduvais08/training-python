# import calculator_102

# calculator = calculator_102.Calculator()

# print(calculator.add(2))

# print(calculator.add(12))

# from text_to_speech import speak

# speak("Please do coding daily", "en", save=True, file="Hello-World.mp3", speak=False)

import mysql.connector
cnx = mysql.connector.connect(user='root', password='uvais',
                              host='127.0.0.1',
                              database='store')
cursor = cnx.cursor()

# print(cnx)

add_country = ("INSERT INTO country (country_name) VALUES (%s)")

# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

# # Insert new employee
cursor.execute(add_country, ('Canada',))
cnx.commit()
