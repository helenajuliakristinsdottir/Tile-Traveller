#Code Listing 2.1-2.6
#1. Rake the numver of points one team is ahed
points_str=input('Enter the lead in points')
points_ahead_int=int(points_str) #breyti í heiltölu

#2. Subtract three
lead_calculation_float=float(points_ahead_int-3) #þurfum á eftir að draga frá 0.5 þess vegna breytum við í float hér

#3 Add a hald-point if the team that is ahead has the ball
#and subtract a half-point if the other team has the ball
has_ball_str=input('Does the lead team have the ball (Yes or No): ')
if has_ball_str=='Yes':
    lead_calculation_float=lead_calculation_float +0.5
else:
    lead_calculation_float=lead_calculation_float -0.5

# Numbers less than zero become zero
if lead_calculation_float <0:
    lead_calculation_float=0

#4. Square that
lead_calculation_float=lead_calculation_float**2

#5. If the result is greater than the number of seconds left in the game,
# the lead is safe.
seconds_remaining_int = int(input("Enter the number of seconds remaining: "))
if lead_calculation_float > seconds_remaining_int:
    print("Lead is safe.")
else:
    print("Lead is not safe.")
