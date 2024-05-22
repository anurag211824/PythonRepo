print(4+5)#add
print(5-3)#sub
print(5*3)#multiply
print(6/2)#divide
print(5//2)#division without showing points
print(5%2)#mod
print(7**3)#pow(7,3) like in c++
print()

#Typecasting

#1.Implicit typeCasting
x = 10    # Integer
y = 5.2   # Floating-point number

# Implicit type casting during addition
result = x + y#The integer `x` is implicitly converted to a float
print(result) #Output:15.2 
#Implicit type casting typically happens when a less precise data type is converted to a more precise data type

#2.Explicit typeCasting
a = 10      #Integer
b = "20"    #String

# Explicit type casting using int()
b= int(b) #The string `y` is explicitly converted to an integer
result = a+b
print(result)# Output:30
#the string value y is explicitly converted to an integer using the int() function before performing the addition operation with the integer value x.
