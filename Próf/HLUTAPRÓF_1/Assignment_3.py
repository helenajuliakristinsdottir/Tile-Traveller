#Dæmi 1
#Printing integers
#Write a program using a while statement, that given an integer as input,
#prints all the integers starting from 1 up to but not including that number.
#Print one number per line.
#For example if the input is
#4
#the output should be:
#1
#2
#3
int = int(input('Input an int: '))
count=1
while int > count:
    print(count)
    count +=1


#Dæmi 2
#Write a program using a while statement, that given the number n as input,
#prints the first n odd numbers starting from 1.
#For example if the input is
#4
#The output will be:
#1
#3
#5
#7
n = int(input('Input an int: ')) 
count = 1
while count < 2*n:
    print(count)
    count += 2


#Dæmi 3
#Write a program using a while statement, that given a series of numbers as input,
#adds them up until the input is 10 and then prints the total.
#Do not add the final 10.
#For example, if the following numbers are input
#8
#3
#11
#10
#The output should be:
#22
num= int(input('Input an int: '))
summa=0
while num != 10:
    summa += num
    num= int(input('Input an int: '))
else:
    print(summa)


#Dæmi 4
#Write a program using a while statement, that given an int as the input,
#prints all the factors of that number, one in each line.
#For example, if the input is
#15
#The output will be
#1
#3
#5
#15
n = int(input("Input an int: ")) # Do not change this line

count = 1
# Fill in the missing code below
while count <= n:
    if n % count == 0:
        print(count)
        
    count += 1


#Dæmi 5
#A prime number is a whole number greater than 1 whose only factors are 1 and itself.
#Write a program using a while statement, that given an int as the input,
#prints out "Prime" if the int is a prime number, otherwise it prints "Not prime".

num = int(input('Input a number: '))
count = 2
prime=True
while count < num:
    if num%count ==0:
        prime=False
    
    count += 1

if prime:
    print('Prime')
else:
    print('Not prime')

#Dæmi 6
#Write a program using a while statement, that finds the only two-digit number where the following applies:
#When you square it, the resulting three-digit number has its rightmost two digits the same as the original two-digit number.
#That is, for a number in the form AB:
#AB * AB = CAB, for some C.
count = 10
while count < 100:
    if (count*count)%100 == count:
        print(count)
        break
    count += 1

#Dæmi 7
#In golf, pars for a hole range from 3 to 5.
#Write a program using a while statement that allows the user to input the par and the score for each of the 18 holes.
#Based on the number of shots compared to par, the program writes out the following:
    #"invalid score", for less than 3 under par
    #"albatross", for 3 under par
    #"eagle", for 2 under par
    #"birdie", for 1 under par
    #"par", for par (neutral e.g. 4 on a par 4 hole)
    #"bogey", for 1 over par
    #"double bogey", for 2 over par
    #"triple bogey", for 3 over par
    #"bad hole", for scores more than 3 over par
#The input/output should look like this:
#Par of hole 1: 5
#Score on hole 1: 6
#bogey
#Par of hole 2: 4
#Score on hole 2: 4
#par
#Par of hole 3: 3
#Score on hole 3: 5
#double bogey
#Par of hole 4: 4
#Score on hole 4: 3
#birdie
#etc.
count = 1
while count <19:
    par = int(input("Par of hole " + str(count) + ": "))
    score = int(input("Score on hole " + str(count) + ": "))
    if par-score>3:
        print('invalid score')
    elif par-score==3 :
        print("albatross")
    elif par-score==2:
        print("eagle")
    elif par-score==1:
        print("birdie")
    elif par-score == 0:
        print('par')
    elif score-par==1:
        print("bogey")
    elif score-par==2:
        print("double bogey")
    elif score-par==3:
        print("triple bogey")
    else:
        print("bad hole")
    count+=1
    


