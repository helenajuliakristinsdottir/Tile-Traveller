#Dæmi 1
#Write a Python program using a for loop that, given an integer as input, prints all the integers starting from 1 up to but not including that number. Print one number per line.
#For example if the input is:
#4
#the output should be:
#1
#2
#3
num = int(input('Input a number: '))
for i in range(1,num):
    print(i)


#Dæmi 2
#Write a program using a for loop, that given the number n as input,
#prints the first n odd numbers starting from 1.
#For example if the input is
#4
#The output will be:
#1
#3
#5
#7
num = int(input('Input a number: '))
for i in range(1,num*2,2):
    print(i)

#Dæmi 3
#If a chessboard were to have wheat placed upon each square such that one grain were placed on the first square, two on the second,
#four on the third, and so on (doubling the number of grains on each subsequent square),
#how many grains of wheat would be on the chessboard at the finish?
#Write a Python program using a for loop that calculates and prints out this number of grains.

total_sum = 0
for i in range(0,64):
    total_sum += 2**i
print(total_sum)

#Dæmi 4
#Write a Python program using a for loop, tthat given two integers as input, prints the greatest common divisor (GCD) of them.
#GCD is the largest integer that divides each of the two integers.
#For example, given the numbers 12 and 15, the output will be:
#3
m = int(input('Input the first integer: '))
n = int(input('Input the second integer: '))

largest=0
if m>n:
    for i in range(1,m):
        if m % i == 0 and n % i == 0:
            largest=i #get haft if setningu hér if i>largest þá largest=i en held það sé óþarfi
else:
    for i in range(1,n):
        if m % i == 0 and n % i == 0:
            largest=i
print(largest)

#Dæmi 5
#Write a Python program using for loops that, given an integer n as input, prints all consecutive sums from 1 to n.
#For example, if 5 is entered, the program will print five sums of consecutive numbers:
#1 = 1
#1 + 2 = 3
#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 = 10
#1 + 2 + 3 + 4 + 5 = 15
#Print only each sum, not the arithmetic expression.
num = int(input('Input a number'))
summa=0
for i in range(1,num+1):
    summa += i
    print(summa)

#Dæmi 6
#Write a Python program using for loops that, given an integer n, prints all the perfect numbers from 1 to n.
#A perfect number is an integer whose sum of integer divisiors (excluding the number itself) add up to the number.
#For example, 6 is a perfect number because the sum of its integer divisors (1+2+3) is equal to 6.

top_num = int(input("Upper number for the range: ")) # Do not change this line
s=0
n=0
for i in range(1,top_num):
    if n<top_num:
        if i%2==1 or i==2:
            n=2**(i-1)*(2**(i)-1)
            if n<=top_num and n!=1:
                print(n)
