top_num = int(input("Upper number for the range: ")) # Do not change this line

divisor=1
sum_of_divisors=0
for i in range(1,top_num+1):
    if top_num % i == 0:
        sum_of_divisors += i
    if top_num == sum_of_divisors: 
        print(i)
