# tem=" "
# count=1
# for i in range(1,n+1):
#     count=i*count
#     print(count)


# fib1=0
# fib2=1
# tem=fib1
# i=1
# while i<n+1:
#     print(tem)
    
#     fib1=fib2
#     fib2=tem
#     tem=fib1+fib2
#     i+=1

# for i in n:
#     tem=i+n
    
#     print(tem,end=" ")

# tem=n.lower()
# print(tem)
# for i in range(1,100):
#  print(i)           

"""
k=list(range(1,10))
print(k)
y="hello i am krishna mohan"
print(y.split())
i=0
tem=''
tem1=[]
while i<len(y):
    print(i)
    tem+=i
    number4 = tem1[tem]
    # lis=[list(i)]
    print(number4)
    i+=1
    # i got a dought why cant we store the values in list
"""

# o=[1,2,34,5,56]
# print(dir(o))
# t=[3,4]
# # o.append(t)
# print(o)
# o.extend(t)
# print(o)
# o.sort()
# print(o)
# o.remove(34)
# print(o)
# o.insert(1,100)
# print(o)
# o.reverse()
# print(o)
# o.sort
# print(o)
# # o.extend(101,44,77,89)
# print(o)123

# o.sort(reverse=True)
# print(o)
 
"""q=list(input("enter the list"))
print(q)
"""
# a = []
# n= int(input("enter the numbers in list: "))
# for i in range(0,n):
#     tem=int(input())
#     a.append(tem)
#     print(a)
#     a.sort()
#     print(type(a))

# l1=list(input("enter the elements"))
# if l1==l1.sort():
#     print(True)
# else :
#     print(False)


# List2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
# for i in List2:
#         if i % 2==0:
#             print(f'even number {i}')
#         else:
#             print("odd number",i)
    
    
a=[1,2]
b=[1,2]
a=b
a+=[6,7]
print(id(a))
print(id(b))
# a=[5,6]

print(a)
print(b)
a=[2,4,7,8,9]
m=a+["km"]
print(m*3)



k=[1,3,2]
m=[1,3,1]
print(max(k))
print(min(k))
print(k>=m)
o=k+m
print(o)
print(ord('a'))
print(11 in k)
# k.split()
print(k)
i="krishna mohan is in techstar"
print(i.split())
print(i)



s=[x*x for x in range(1,11)]
print(s)
l= [x for x in s if x%2==0 ]
print(l)


t=(1,2,3,4,5,6,7,1)
print(t.count(1))
print(t.index(7))
print(t[3::])
print(min(t))
 

# q=list(eval(input("enter the list use , for every element")))

# print(q) 
# q.sort()
# print(q)
# print(sorted(q))
#SET METHODS()
z=set()
print(type(z))
z={1,2,10,4,15,36}
print(z)
z.add(100)
print(z)
z.remove(100)
print(z)
print(z.pop())
print(z)

print(z)
f=[99,22,45,756]
l=[999,444,10,15]
z.update(f,l)
z.update([12,'000'])
print(z)
z.union(f)
print(z)
t1={1,2,3,4,5}
t2={4,5,6,7,8}
print(t1)
print(t1.intersection(t2))
print(t1.difference(t2))
print(t1)