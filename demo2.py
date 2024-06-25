# INTRODUCTION TO LIST
"""
list = [11,3,6,8,8888,55,101]
#print(max(list))
max = list[0]
for i in list:
    if i >max:
        max = i
        print(max)
"""
#LIST
"""
list = [2,4,5,6,6,3,8,8,9]
repeat = []
for i in list:
    if i not in repeat:
        repeat.append(i)
        repeat.sort()
        print(repeat) 
"""
#PACKING AND UNPACKING IN LIST
"""
tuple = [1,5,9]
x,y,z = tuple
print(y)
"""    
#DICTIONARY
"""    
customer = {
    "name" : "krishna",
    "age": 22,
    "is-verified" : True
}
customer["school"]= "mohan public school"
print(customer["school"])
print(type(customer))
"""
#DICTIONARY
"""
phone_no=input("enter the number")
names = {
    "1" : "one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten"}
output= ""
for i in phone_no:
    output += names.get(i,"!") + " "
print(output)
"""
#DEFINING A FUNTION
"""
def greet_user(name):
    print(f'hi  {name}')
    print("its krishna")
    
print("its intro")
greet_user("mohan")
print("finesh")
"""
#FUNTION OPERATIONS
"""
def Square(number):
    return number*number
result =Square(10) 
print(result)    
"""
#FUNTION OPERATIONS 
"""
def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight/0.45 


print(lbs_to_kg(76))
print(kg_to_lbs(79))
"""