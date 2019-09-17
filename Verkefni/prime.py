n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
prime = True
count = 1
while count <= n:
    if n%count == 0:
        if count != 1 and n != count:
            prime = False
    count +=1
    
    
if prime:        
    print("Prime")
else:
    print("Not Prime")
