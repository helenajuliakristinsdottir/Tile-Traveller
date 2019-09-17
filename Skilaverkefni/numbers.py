#1. Finnur og skrifar út allar pósítívar tveggja stafa tölur sem eru þannig að 
       #annað veldi af summu einstakra tölustafa er jafnt tölunni sjálfri.
#2. Finnur og skrifar út allar pósítivar tölur < 100 sem eiga sér nákvæmlega 10 deila (e. divisors)

#Sérhver tala sem forritið finnur og uppfyllir ofangreind skilyrði er skrifuð út í sér línu.

count = 10
max_int=100


while count < max_int:
    x=count//10 #finnur fyrri töluna
    y=count%10 #finnur seinni töluna
    if (x+y)**2 == count:
       print(count)
    count += 1


divisor=1
sum_of_divisors = 0


#veit að þetta virkar til að finna fjölda divisors og prenta út töluna
num=48
while divisor <= num:
    if num % divisor == 0:
        sum_of_divisors += 1 
    divisor += 1
if sum_of_divisors >= 10:
    print(num)



    
