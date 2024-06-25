# WRITE A PROGRAM TO PING BIGGEST OF 3 NUMBERS
"""
num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))

if (num1>=num2) and (num1>=num3):
    print(f'largest number is num1  {num1}')
elif (num2>=num1) and (num2>=num3):
    print(f'largest number is num2  {num2}')
else:
    print(f'largest number is num3  {num3}')
    """

#LOGIC FINDING BIGGEST NUMBER?

#WRITE A PROGRAM TO PRING THE SMALLEST OF 3 NUMBER
"""
num1=eval(input("enter the number"))
num2=eval(input("enter the number"))
num3=eval(input("enter the number"))
if num1<num2 and num1<num3:
    print(f'smallest number is num1  {num1}')
elif num2<num1 and num2<num3:
    print(f'smallest number is num2  {num2}')
else:
    print(f'smallest number is num3  {num3}')
     
"""

#FACTORIAL
"""
 num = int(input("enter the number"))
 n=1
 for i in range(1,num+1):
    n= n*i 
 print(n)
"""
#FIBONNACCI
"""
n= int(input("enter a number"))
fib1=0
fib2=1
i=1
nex_num=fib1 
while i<=n:
    print(0+nex_num,end=" ")
   
    fib1  = fib2
    fib2= nex_num
    nex_num=fib1+fib2
    i+=1
"""

# input a2b3c4 output:acbecg
"""
n= str(input("enter the data"))
op=""
for i in n :
    if i.isalpha():
        op+=i
        p=i
    else:
        op=op+chr(ord(p)+int(i ))
print(op)
"""

#METHODS IN PYTHON
"""
a="hi krishna mohan this is surya"
print(a.capitalize())
print(a)
print(a.center(50,'*'))
b= "pYTHon"
print(b.casefold())
print(a.count('2'))
print(a.title())

print(chr(80))
"""
#INPUT :a4b3c4  OUTPUT:aaaaabbbbccccc
be=input("enter  elements")
tem=""
for i in be:
    if i.isalpha():
        tem+=i
        prev = i
    else:
        tem += prev*int(i)
print(tem)
                

# num= input("enter the data")
# tem=""
# for i in num:

#     if i.isalpha():
#         tem+=i
#         p=i
#     else:
#         # tem=tem*tem

#      print(ord(i))
        
# print(tem)

#INPUT :b5c6d2  OUTPUT:bcd256

# n= input("enter the data")
# tem=""
# for i in n:
#     if i.isalpha():
#        tem+=i
#        p=i
#     else:
#         tem= tem+p
# print(tem)

#LIST METHODS
"""
o=[1,2,34,5,56]
print(dir(o))
t=[3,4]
# o.append(t)
print(o)
o.extend(t)
print(o)
o.sort()
print(o)
o.remove(34)
print(o)
o.insert(1,100)
print(o)
o.reverse()
print(o)
o.sort
print(o)
# o.extend(101,44,77,89)
print(o)
o.sort(reverse=True)
print(o)    

"""
# Porgam to check List is in ascending order or not
 # List1 = [1, 2, 3, 5, 4, 1, 7, 9] 
#I GOT A ERROR BY USING INPUT METHOD
 

"""
q=list(eval(input("enter the list use , for every element")))

if q==q.sort():
    print(True)
else :
    print(False)
"""
#Program to Find Even Numbers From a List
# List2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]

#I AM NOT SATISFIED WITH THIS METHOD
"""

List2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
for i in List2:
        if i % 2==0:
            print(f'even number {i}')
        else:
            print("odd number",i)    
    
"""


# Program to Merge Two Lists

"""
List3 = [1, 2, 4, 6]
List4 = [9, 3, 19, 7]
List3.extend(List4)
print(List3)
""" 

#Interchange First and Last Element of a List
 #List5 = [1, 29, 51, 9, 17, 6, 7, 23]
"""_summary_
    """
#5) Program to Subtract a List from Another List
"""a = [1, 2, 3, 5]
b= [1, 2]
C=list
C=a-b
print(C)
"""
# EVEN OR ODD
s=[ x for x in range(1,40)]
k=[x for x in s if x%2==0 ]
m=[x for x in s if x%2!=0]
print(f'The numbers in the list are even\n   {k}\n\n')

print(f'The numbers in the list are odd\n    {m}')

        




