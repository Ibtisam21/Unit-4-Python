# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month of the year (e.g. Jan, Feb etc.): ")
day = int(input("Input the day: "))

if month in ('Jan', 'Feb', 'Mar'):
	season = 'winter'
elif month in ('Apr', 'May', 'Jun'):
	season = 'spring'
elif month in ('Jul', 'Aug', 'Sept'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'Mar') and (day > 19):
	season = 'spring'
elif (month == 'Jun') and (day > 20):
	season = 'summer'
elif (month == 'Sept') and (day > 21):
	season = 'autumn'
elif (month == 'Dec') and (day > 20):
	season = 'winter'

print("Season is",season)