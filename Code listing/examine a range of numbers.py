#examine a range of numbers

#classify a range of number with respect to perfect, abundant or deficient
#unless otherwise stated, variables are assumed to be of type int

top_num = int(input('What is the upper number for the range:'))
number=2

while number <= top_num:
    #sum the divisors of number
    #classify the number based on its divisor sum
    divisor=1
    sum_of_divisors=0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors= sum_of_divisors + divisor
        divisor = divisor + 1

# ef sum_of_divisors er stærra en numerið, numerið er abundant
# ef sum_of_divisors er minna en numerið, numerið er deficient
#otherwise þá er það perfect

# classify the number base on its divisor sum
    if number == sum_of_divisors:
        print(number,'is perfect')
    if number <sum_of_divisors:
        print(number, 'is abundant')
    if number > sum_of_divisors:
        print(number, 'is deficient')
    number += 1 #number = number + 1
