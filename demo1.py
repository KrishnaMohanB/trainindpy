
#WHILE LOOP
""" 
i = 1
while i <= 5:
     print(i)
     i = i + 1
print("done")
"""
#WHILE LOOP
"""      
special_number= 9
i=0
while i<3 :
    num= int (input("enter the number  :"))
    i=i+1
    if num==special_number:
        print("you won!")
        break
print("BETTER LUCK NEXT TIME")
"""
#WHILE LOOP SMALL EXERCISE
"""    
command = ""
started = False
while True:
    command = input("enter command !")
    if  command == "start":
        if started:
            print("car is already started")
        else:
            print("car is starting")
            print("car is started")
    elif command == "stop":
        print("car is stoped")
    elif command=="help":
        print("""#Start - to start the car
#stop - to stop the car
#quit -to quit 
""")
    elif command=="quit":
        print("quit!")
        break
    else:
      print("sorry i dont understand")
"""
#FOR LOOP
"""
box = [10,20,30]
add = 0   
for i in box:
     add += i
     print(add)
"""
#FOR LOOP
"""
for x in range(5):
    for y in range(4):
        print (f'({x},{y})\t',end=" ") 
"""
#FOR LOOP
"""
num = [5,2,5,2,2]
for i in num:
    i= i* '*'
    print(i)
"""
