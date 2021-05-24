"""24May"""
print("hello World")
print('hello World')
"""
Declaring Variables
*variable=value
*n=5
"""
n=1
print(n)
print(n*2)
p=n
print(p)

"""
Data Types
*Integer
*Float
*String
*Boolean
*Complex
*List
*Dictionary
*Tuple
*Set
"""

#String
hello="world"

print(hello)#print variable
print("world")#print value
print(n)

#type
print (type(hello))#print data type

#Integer
int_value=5
print (int_value)
print(type(int_value))

#Float
t=2.19
print(type(t))

print(type('x'))

#Boolean
t,f = True , False
print(type(t))
print(t)
print(f)

#Swapping
data1=7
data2=12
data3=23
data4=33
data1,data2,data3,data4 = data2, data1, data4, data3
print(data1,data2,data3,data4)

print(data1)
print("data1")
print("data1",data1, "data2", data2)

#Length
print(len("I love Python"))

name="Nurhayat"
print("hello{}".format(name))

data12 = 5
data13 = 90
print("My value:{} and Your value:{}".format(data12, data13))

data12 = 5
data13 = 90
print("My value:{} and Your value:{}".format(data12, data13))
print(f'My value: {data12} and your value: {data13}')
print("My value:" + str(data12) + "Your Value:" + str(data13))

a=50
print(type(a))
a=str(a)
print(type(a))
#print(world + str(len(world)))
#print(world + " " + str(len(world)))
print(float(5))

#Aritmetic Operations
print(5**2)
print(5**3)
print(35+67)
print("35"+"67")
print("Nur"+"hayat")
print("35"*3)
print("hello"*4)


x = 10
print(x+2)
print(x-2)
print(x*2)
print(x**2)
print(x**4)
print(x/2)
print(x//2)
print(x%2)

x=45
y = 13
print(y/2)
print(y//2)
print(y % 2)

z = 5
z+=1 # this statement equals to z= z+1 , meaning while the previous value of z is 5, the new z value becomes 6.
print(z)
z +=2 #z = z + 2
print(z)
z*=2 # z = z * 2
print(z)

print(t)
print(f)
print(t or f)
print(t and f)
print(not t) # not: True if operand is false (complements the operand)
print(t != f) # != not equal
print(t==f) # equal

#Indexing and Slicing

hello = "Hello"
print(hello)
print(hello[0])
print(hello[1])
print(hello[2])
print(hello[3])
print(hello[4])

hello2 = " Hello"
hello2[0]

world="world"
print(world)
print(world[-1])
print(world[-3])
print(world[-5])

job = " Engineering"
print(job[-5])

print(hello[2:4]) # [x:y] --> take the values from x th to y th but don't take y th value.
print(world[1:4])
print(world[3:5])
print(world[3:])
print(hello[2:len(world)])

print(world[2:4:1])# [start:end:step]
city = "istanbul"
print(city[0:6:2])
#in
print("y" in city)
print("anb" in city)

m = 8
print(float(m), m)

ai = 'artificial' + ' ' + 'intelligence'
print(ai)

word = 'machine learning'
print(word.capitalize())
print(word.upper())
print(word.replace('machine','artificial'))
word2 = " artificial general intelligence"
print(word2.strip())

y = input("Please enter a city name: ") #input method always takes string type.
print(y)
print(type(y))

month = 12
day = 365
print('One year is ', month, 'months, and ', day, 'days.', sep =' ')
print('One year is ', month, ' months, and ', day, ' days.', sep ='')
print("One year is " + str(month) + " months, and " + str(day) + " days.")