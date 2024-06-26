# PRACTICING INPUT

print("hello")
#name = input("enter name")
#age = input("Enter Age")
Patient = input("old or new")

print(name)
print(age)
print(Patient)
"""
#FIND AGE WITH YEAR
"""
Year_birth=input("enter your birth year")
age = 2024 - int(Year_birth)
print(age)
"""
#FINDING AGE USING DATETIME LIBRARY
"""
import datetime
Year_birth=input("enter your birth year")
Current_Year= datetime.date.today().year
age = Current_Year - int(Year_birth)
print(age)
"""
#CONVERTING WEIGHT POUNDS TO KG
"""
weight_pounds=input("enter the weight in pounds")
weight_kg = float(weight_pounds) * 0.453592
print(float(weight_kg))
"""
#INDEXING
"""
x= "krishna mohan"
print(x[-1])
"""
#LOWER & UPPER
"""
x1= "krishna mohan"
print(x1.upper())
print(x1.lower())
"""
#IF & ELSE CONDETION
"""
hot_temp= True

if hot_temp :
    print("its a hot day")
    print("drink plentyof water")
else :
    print("its a cold day")
    print("wear sweather")
print("have a great day")
"""
#IF & ELSE CONDETION
"""
price = 1000000
good_creadit= False
if good_creadit :
    print("put down 10% ")
else:
    print("put down 20%")
"""
#IF & ELSE CONDETION
"""
Name = input("enter the name")
if len(Name) < 3:
      print("name atleast shoud have 3 characturs")
elif len(Name) > 50 :
      print("namecant execed 50 characturs")
else :
      print("name looks good") 
""" 

     
