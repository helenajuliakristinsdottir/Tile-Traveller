#calculate the area and circumference of a circle from its radium
#step 1: promt for a radius
#step 2: apply the area formula
#step 3: Print out the results

import math
radius_str=input("Enter the radius of your circle: ")
radius_int=int(radius_str)
circumference=2*math.pi*radius_int
area=math.pi*(radius_int**2)
print("The cirumfence is:",circumference, \
      ", and the area is:", area)



#auka
#my_var=float(my_var) #covert string to a float(floting point)
