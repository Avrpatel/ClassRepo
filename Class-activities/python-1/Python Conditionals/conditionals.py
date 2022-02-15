# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("Oooo needs some work")

# this statement is false and will print the else statment


# 2.
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
    
#this statement is true and will print the if statement 

# 3.
age = 21
if age > 20:
    print("You are of drinking age!")
else:
    print("Argggggh! You think you can hoodwink me, matey?! You're too young to drink!")

#this statement is true and will print the if statement        
    
# 4.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 4!")
else:
    print("Oh good you can count")
    
#this is a true statement and will print the if statement 
    


# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")

#This statment is false and will print the else statement i.e stick to the lazy river 