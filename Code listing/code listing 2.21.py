# sum up a series of even numbers
# make sure user input is only even numbers
# variable names without types are integers . Rule 4

print ("Allow the user to enter a series of even integers. Sum them.")
print ("Ignore non-even input. End input with a '.'")
# initialize the input number and the sum
number_str = input("Number: ")
the_sum=0
#Stop if a period (.) is entered .
# remember , number str is a string until we convert it
while number_str != ".":
    number = int(number_str)
    if number%2==1: #numberisnoteven(itisodd)
        print ("Error, only even numbers please.")
    else:
        the_sum += number
    number_str = input("Number: ")
    
 #set hér else í staðin fyrir continue því einfaldara að nota það            
        #number_str = input("Number: ")
        #continue     # if the number is not even , ignore it
    #the_sum += number
    #number_str = input("Number: ")

print ("The sum is:",the_sum)