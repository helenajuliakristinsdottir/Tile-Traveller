for i in range(10,100):
    first_number = i % 10
    last_number = i // 10
    if (first_number+last_number)**2 == i:
        print(i)
        
for x in range(1,100):
    number_of_divisors = 0
    for i in range(1,100):
        if x % i == 0:
            number_of_divisors += 1
        if i == 99:
            if number_of_divisors == 10:
                print(x)
                