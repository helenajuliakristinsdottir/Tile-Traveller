# Dæmi 1
#num1=int(input('Input a number: '))
#num2=int(input('Input another number: '))
#summa=num1+num2
#print(summa)

# Dæmi 2
#num1=int(input('Input a number: '))
#num2=int(input('Input another number: '))
#num3=int(input('Input a third number: '))
#summa=num1+num2+num3
#print(summa)

# Dæmi 3
#intiger=input('Input a intiger: ')
#intiger2=input('Input another intiger: ')
#resault=intiger*intiger2
#print(resault)

# Dæmi 4
#name=input('Input a name: ')
#age=int(input('Input an age: '))
#print('Hello my name is',name,'and my age is',age, 'where',name,'and',age,'are the values that were input')

# Dæmi 5
#firstname=input('Input a firstname: ')
#lastname=input('Input a lastname: ')
#fullname=firstname + " " + lastname
#print('Your full name is',fullname,'where',fullname,'is the value og the variable',fullname)

# Dæmi 6
#celsius=float(input('Enter a temerature in celsius: '))
#Fahrenheit=float(celsius*(9/5)+32)
#print(Fahrenheit)

#Dæmi 7
#num1=int(input('Input a number: '))
#num2=int(input('Input another number: '))
#large=num1
#if num2>large:
    #large=num2
    #print(large)
#elif num2==large:
    #print('The numbers are equal')
#else:
    #print(large)

#Dæmi 8
#inp=input('Enter a string: ')
#ind=input('Enter another string: ')
#if len(inp)==len(ind): #len er lengd
    #print('The strings are the same lenght')

# Dæmi 9
#inp=int(input('Enter a number: '))
#ind=int(input('Enter another number: '))
#ink=int(input('Enter yet another number: '))
#minimum = inp
#if ind < minimum:
    #minimum = ind
#elif ink < minimum:
    #minimum = ink
#print(minimum)

#Dæmi 10
#a=int(input('Input an integer: '))
#if 0 < a < 10:
    #print('Less than 10')
#elif 10 <= a < 20:
    #print('between 10 and 20')
#elif 20<=a:
    #print('the value is too high!')
#else:
    #print('too low')

#Dæmi 11
#a=int(input('Enter an integer: '))
#b=int(input('Enter another integer: '))
#choice=int(input('Enter yet another integer: '))
#summa=0
#if choice==1:
    #summa=a+b
    #print(summa)
#elif choice==2:
    #summa=a-b
    #print(summa)
#elif choice==3:
    #summa= a*b
    #print(summma)
#else:
    #print('Invalid input')

#Dæmi 12
#for i in range(1,11):
    #print(i)

#count=1
#while count <= 10:
    #print(count)
    #count += 1

#Dæmi 13
#for i in range(-5,11):
    #print(i)
#count = -5
#while count<=10:
    #print(count)
    #count += 1

#Dæmi 14
#for i in range(3,14):
    #print(i*2)

#count=3
#while count <= 13:
#    print(count*2)
#    count += 1

#Dæmi 15
#multiplier = int(input('Input a intiger: '))
#for i in range(2,16):
#    print(i*multiplier)
#count=2
#while count<=15:
#    print(count*multiplier)
#    count += 1

#Dæmi 16
#for i in range(10,-1,-1):
#    print(i)

#count=10
#while count >= 0:
#    print(count)
#    count -= 1

#Dæmi 17
#for i in range(15,2,-2):
#    print(i)

#count=15
#while count >=3:
#    print(count)
#    count -= 2

#Dæmi 18
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#count=low
#while count<=high: #eða while low <=high
#    print(count) #print(low)
#    count += 1 #low += 1

#for i in range(low,high+1):
#    print(i)

#Dæmi 19
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#if low<high:
    #for i in range(low,high+1):
        #print(i)
    #while low<=high:
        #print(low)
        #low += 1

#Dæmi 20
#turns=int(input('Input an integer: '))
#count=1
#while count<=turns:
    #a=int(input('Input an integer: '))
    #print('you picked',a)
    #count += 1
#for i in range(turns):
    #a=int(input('Input an integer: '))
    #print('you picked',a)

#Dæmi 21
#turns=int(input('Input an integer: '))
#count=1
#while count<=turns:
    #a=int(input('Input an integer: '))
    #if a % 2 ==1:
     #   print('you picked',a)
    #count += 1
#for i in range(turns):
    #a=int(input('Input an integer: '))
    #if a % 2 == 1:
        #print('you picked',a)

#Dæmi 22
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#summa=0
#for i in range(low,high+1):
    #summa += i
#print(summa)

#count=low
#while count <= high:
    #summa += count
    #count += 1
#print(summa)

#Dæmi 23
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#summa=0
#for i in range(low,high+1):
    #if i % 2 == 1:
        #summa += i
#print(summa)
#count=low
#while count<=high:
    #if count % 2 == 1:
        #summa += count
    #count += 1
#print(summa)

#Dæmi 24
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#summa=0
#for i in range(low,high+1):
    #if i % 3 == 0:
        #summa += i
#print(summa)

#Dæmi 25
#low=int(input('Input a low intiger: '))
#high=int(input('Input a high intiger: '))
#summa=0
#for i in range(low,high+1):
    #if i % 3 == 0 or i % 5 == 0:
        #summa += i
#print(summa)

#Dæmi 26
#turns=int(input('Input an intiger: '))
#count=1
#neikvætt=0
#while count<=turns:
    #a=int(input('Input an intiger: '))
    #if a<0:
        #neikvætt += 1
    #count += 1
#print(neikvætt)

#Dæmi 27
#turns=int(input('Input an intiger: '))
#count=1
#summa=0
#while count<=turns:
    #a=int(input('Input an intiger: '))
    #if a<0:
        #summa += a
    #count += 1
#print(summa)
    
#Dæmi 28
#turns=int(input('Input an intiger: '))
#count=1
#neikvætt=0
#jákvætt=0
#while count<=turns:
    #a=int(input('Input an intiger: '))
    #if a<0:
        #neikvætt += 1
    #if a>0:
        #jákvætt += 1
    #count += 1
#print("You picked", neikvætt, "negative integers")
#print("You picked", jákvætt, "positive integers")


#Dæmi 29
#turns=int(input('Input an intiger: '))
#count=1
#summan=0
#neikvætt=0
#summaj=0
#jákvætt=0
#while count<=turns:
    #a=int(input('Input an intiger: '))
    #if a<0:
        #neikvætt += 1
        #summan += a
    #if a>0:
        #jákvætt += 1
        #summaj += a
    #count += 1
#print("You picked", neikvætt, "negative integers")
#print("You picked", jákvætt, "positive integers")
#print("The sum of negatives:", summan)
#print("The sum of positives:", summaj)