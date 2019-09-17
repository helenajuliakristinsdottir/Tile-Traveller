#leikur, að giska á rétta tölu
#while-else
#Simple guessing game: start við a random numer and guess with hints until:
    #Guess is correct
    #the guess is out of range indicating the user is quitting
#All non-typed variables ar integers

import random #get the random number module
number = random.randint(0,100) #get a random number, milli 0 og 100 að meðtöldum 0 og 100, random integer

print('Hi-Lo Number Guessing Game: between 0 and 100 inclusive.')
print()

#get an initial guess
guess_str = input('Guess a number: ')
guess=int(guess_str)

#while guess is range, keep asking

while 0 <= guess <= 100:
    if guess > number:
        print('Guessed Too High.')
    elif guess < number:
        print('Guessed Too Low.')
    else:
        print('You guessed it. The number was:',number)
        break #þá skippa ég else suitið á while lykkjunni og fer út úr öllu
    #keep going, get the next guess
    guess_str = input('Guess a number: ')
    guess=int(guess_str)
else:
    print('You quit early, the number was:',number)
