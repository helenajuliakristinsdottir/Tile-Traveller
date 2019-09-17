# Dæmi 1
#true or false
#In Python, an empty object (0 for int, 0.0 for float, '' for string) is considered to be False;
#all non-empty objects are considered to be True.
#Write a program that prompts for an integer and prints out True if it is considered True, otherwise it prints False.
num_int=int(input('Input a number:'))

if num_int!=0 and num_int!='':
    print(True)
else:
    print(False)


#Dæmi 2
#Write a program that prompts for a number.
#If it is a negative number, print 'Negative',
#it it is a positive number, print 'Positive', and if the input is 0, the print 'Zero'.
num=int(input('Input a number:'))

if num<0:
    print('Negative')
elif num==0:
    print('Zero')
else:
    print('Positive')


#Dæmi 3
#Write a program that reads in 3 integers and prints out the maximum of the three.
num1 = int(input('First number:'))
num2 = int(input('Second number:'))
num3 = int(input('Third number:'))

largest = num1
if num2 > largest:
    largest = num2

if num3 > largest:
    largest = num3

print('The maximum is:',largest)


#Dæmi 4
#Write a program that prompts for a grade (a float).
#A valid grade is between 0.0 and 10.0 (both inclusive).
#A passing grade is between 5.0 and 10.0 (both inclusive).
#The program pints out "Invalid grade!", "Passing grade!", or "Failing grade!", depending on the input.
grade = float(input('Input a grade: '))

if grade < 0.0 or grade > 10.0:
    print('Invalid grade!')
elif 5.0 <= grade <= 10.0:
    print('Passig grade!')
else:
    print('Failing grade!')


#Dæmi 5
#Here is an algorithm to determine whether a year is a leap year:
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
 
#Write a program that prompts for a year and prints out True if the year is a leap year, otherwise False.
year = int(input('Input a year: '))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(True)
        else:
            print(False)
    else:
        print(True)
else:
    print(False)

#Dæmi 6
#Accept d1 and d2, the number on two dices as input.
#First, check to see that they are in the proper range for dice (1-6). If not, print the message "Invalid input".
#Otherwise, determine the sum. If the sum is 7 or 11, print "Winner".
#If the sum is 2, 3 or 12, print "Loser". Otherwise print the sum.
d1=int(input('Input first dice: '))
d2=int(input('Input second dice: '))

teningur=d1+d2
if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    if teningur==7 or teningur==11:
        print('Winner')
    elif teningur==2 or teningur==3 or teningur==12:
        print('Loser')
    else:
        print(teningur)

else:
    print('Invalid sum')

#Dæmi 7
#King’s Island needs a program for its admission booths.
#When visitors to the park come up to the booth to purchase their tickets, the worker uses this program to figure out how much to charge them.
#Each ticket cost $30. Senior citizens (age >= 65) are given a 50% discount. Children under (or equal to) the age of 5 get a free admission.
#Write a program that prompts for the visitor's age and computes and prints the ticket price (which should be a float).
age=int(input('Input age: '))
ticket=30.0
if age >= 65:
    price = float(ticket*0.5)
elif age <= 5:
    price = float(0)
else:
    price = ticket
print('ticket price is:',price)


