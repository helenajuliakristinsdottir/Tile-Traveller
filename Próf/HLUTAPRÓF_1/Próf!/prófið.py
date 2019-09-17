age=int(input('Enter your age: '))
if 0 <= age <=34:
    print('Young')
elif 35 <= age <= 50:
    print('Mature')
elif 51 <= age <= 69:
    print('Middle-aged')
elif age >= 70:
    print('Old')
else:
    print('Invalid age')

#Dæmi 3
First=int(input('First: '))
Step=int(input('Step: '))

max_summa = 100 #the maximum sum is when the while should stop
summa = 0

while summa < max_summa:
        print(First,end=' ')
        summa += First
        First += Step #then i get the initial value of the series plus the difference, the next value is the first value+step

print('')
print('Sum of series:',summa)


#Dæmi 4
stars= int(input('Number of stars: ')) #max number of stars

for i in range(1,stars+1):
    for j in range(1,i+1):
        print('*',end='') #the output should be stars in one row and end='' does that
    print('\n',end='') #here I want to get a new line with the next section in i

#sniðugari leið
for i in range(1,stars+1):
    print(i*'*')
