a = 10
ba= 11
c=11
d=10.2
e=10.2
a1= "krishna"
b1="mohan"
b2= 4/ 2
c3= 3/2

print(type(a)) 
print(id(a))
print(id(ba))
print(id(c))
print(f'id of d ={id(d)}')
print(f'id of e ={id(d)}')
print(a1+' ' + b1)
print(c3)
print(type(c3))

#operaters
a= [1,2,3,4]
b4= [1,2,3]
print(a==b4)
y=10
y-=5
print(y)

q="krishna"
w="krishn"
print(q is not w)

print("IN , NOT IN OPERATIONS")
print(2 in b4)

print("TYPE CASTING")

A=10.5
print(complex(A))
import math
import gc
a= 10+3j+2j
b= 10+3j+2j
print(f'id of a is  {id(a)}')
print(f'id of b is {id(a)}')
if id(a)==id(b):
    print("its equal ")
else:
    print("its not equal")
gc.isenabled
print(gc.isenabled)

#INPUT() OUTPUT()
#c=input("enter the name")
#print(f'hi, good morning {c}')

#q= str(input("enter the number "))
#w= str (input("enter the number"))
#print(q+w)
print("i want space")
print("i got space")

k= ""
if k:
    print("hello")
else:
    print("bye")
#LOOP STATETMENTS
s="qwerthjkgfg"
for i in  s:
    print(f'{i}={ord(i)}\t',end=" ")
    print("",end="")
    
    












