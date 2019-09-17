# Dæmi 1
#Einstein's famous equation states that the energy in an object at rest equals its mass times the square of the speed of light.
#(The speed of light is 300,000,000 m/s.)
#Complete the skeleton code below so that it:
#* Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
#* Calculate the energy, e
#* Prints e
c=3*10**8 #speed of light
mass=float(input('Insert mass:'))
e=mass*c**2 #mass times the square of the speed of light
print('e:',e)


#Dæmi 2
#Input a string of digits.
#Convert the string to an int.
#Print the int.
#Convert the string to a float.
#Print the float.
number_int = int(input('Insert a number:'))
print('The number is:',number_int)

number_float = float(number_int)
print('The float number is',number_float)

#Dæmi 3
#Euclidean distance fromula
#the formula to find the distance between two points in a plane.
#You will take the two coordinates as input and output the distance between them.
#Hint: You can use the sqrt function in the math module.
import math
x1=int(input('Insert a distance:'))
x2=int(input('Insert a distance:'))
y1=int(input('Insert a distance:'))
y2=int(input('Insert a distance:'))

#math.hypot(x,y) skilar Euclidean norm, sqrt(x*x+y*y)
x=x2-x1
y=y2-y1

Euclidean=math.hypot(x,y)
print('The Eculidean distance is:',Euclidean)
10


#Dæmi 4
#Body Mass Index
#BMI is a number calculated from a person's weight and height.  The formula for BMI is:
#weight / height2
#where weight is in kilograms and heights is in meters
#Write a program  that prompts for weight in kilograms and height in centimeters and outputs the BMI.
weight = float(input('Weigth (kg):'))
height = float(input('Height (cm):'))

height *= 10**(-2) #eða deilt með 100

BMI=weight/(height**2) 
print('Your BMI is:',BMI)

#Dæmi 5
#Input a six-digit integer.
#Assign first_three (int) to be the first three digits.
#Assign last_two (int) to be the last two digits.
#Assign middle_two (int) to be the middle two digits.
#Print out the three values.
#Hint: use quotient (//) and remainder (%)
#For example, if the input is 123456
#The first three digits: 123
#The last two digits: 56
#The middle two digits: 34

digits=int(input('Input a six digit integer:'))
print('Original input:',digits)
first_three=digits//1000
print('First three:',first_three)
last_two=digits%100
print('Last two:',last_two)
middle_two=digits//100%100
print('Middle two:',middle_two)

#Dæmi 6
#Given seconds (int) calculate hours, minutes, and seconds.
#For example, given 80000 seconds that is
#22 hours, 13 minutes, and 20 seconds.
#Hint 1: use integer division (//) and remainder (%)
#Hint 2: we require that you create and output variables hours, minutes, and seconds, but you will likely find an additional variable useful.

#Time
input=int(input('Input seconds:'))

#hours
hours= input//(60*60)

#minutes
minutes=(input%(60*60))//60

#seconds
secounds=input%60

print(hours,'hours,',minutes,'minutes, and',secounds,'seconds.')
