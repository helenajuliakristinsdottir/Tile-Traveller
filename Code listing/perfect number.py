#perfect number:

#get a number to check
number_str = input('Please enter a number to check:')
number = int(number_str)

#find and sum up the divisors
divisor=1
sum_of_divisors=0
while divisor < number:
    if number % divisor == 0:
        sum_of_divisors= sum_of_divisors + divisor
    divisor = divisor+1

#classify the resault
if sum_of_divisors == 10: #divisor: fyrir tölu N er divisor
#tala sem divides into N evenly, sem þýðir að remainder er 0 N/div=0
    print(number, 'is perfect')
else:
    print(number, 'is not perfect')
