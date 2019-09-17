#Integer sequence project
#Helena Júlía Kristinsdóttir & Silja Björk Axelsdóttir
#Hópur 3

#Góð regla er að setja upphafskylirði áður en while lykkjan byrjar
total = 0 
even = 0
odd = 0
highest_value = 0
num = int(input('Enter an integer: ')) #notandi slær inn gildi

while num > 0:

    total += num #hér plúsast gildin saman sem notandinn slær inn saman
    print('Cumulative total:',total)

    if num%2 == 0: #hér viljum við leita af even numbers
        even += 1
    else: #það sem er ekki even number er oddatala
        odd += 1 

    if num>highest_value: #hér leitum við af hæsta gildinu sem slegið er inn, gildið yfirskrifast alltaf
        highest_value = num
    num = int(input('Enter an integer: ')) #notandi slær inn gildi þar til while verður false

else: #fer inn í else skilyrðið þegar fyrri hlutinn verður false
    if total > 0: #fer þá ekki inn í else í while lykkjunni ef num=0 eða minna
        print('Largest number:',highest_value)
        print('Count of even numbers:',even)
        print('Count of odd numbers:',odd)
    
    
