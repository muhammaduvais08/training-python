# s1 = "Python prOgramming"

# l = len(s1)
# print(l)
# i = 0
# while i < l:
#     if s1[i].lower() != 'a' and s1[i] != 'i' and s1[i] != 'e' and s1[i] != 'o' and s1[i] != 'u' and s1[i] != ' ' :
#         print(s1[i])
#     i += 1 # i = i + 1
    
# s1 = "Python 1 2pr3Ogramming"

# l = len(s1)
# i = 0
# while i < l:
#     if s1[i].lower() not in 'aeiou 1234567890' :
#         print(s1[i])
#     i += 1 # i = i + 1


#write a program to make a string 

s1 = "Pyt3hon 1 2pr3ogra7mming" # Python  prOgramming
s2 = ''
l = len(s1)
i = 0
while i < l:
    if s1[i].lower() not in '1234567890' :
        s2 = s2 + s1[i]
    i += 1 # i = i + 1
    
print(s2)