# # Addition
# add = 30 + 12
# print(add)
#
# # Subtraction
# difference = 30 - 12
# print(difference)
#
# # Multiplication
# product = 30 * 12
# print(product)
#
# # Division
# quotient = 30 / 12
# print(quotient)
#
# # Exercise convert 1042 seconds to minutes and seconds
# seconds = 1042
# display_minutes = seconds / 60
# print(display_minutes)
#
# # Output is 17.366666666667, but we want a non-decimal output.

seconds = 1042
display_minutes = seconds // 60 # a second forward slash will have the expression round down.
print(display_minutes)

# Excellent now we know that 1042 divided by 60 = 17 minutes to find the remainder we incorporate the % modulo operator
seconds = 1042
display_seconds = 1042 % 60
print(display_seconds)

# Converted the variables to a string to add "minutes" and "seconds" after both answers
print(str(display_minutes) + ' minutes')
print(str(display_seconds) + ' seconds')

# Let's explore how we can create a program that can calculate the distance between two planets. '
# We will start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).
# Note: Remove the commas when you're using the values.

# Start by creating two variables named first_planet and second_planet.
# Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.

first_planet = 149597870
second_planet = 778547200

# You have two variables which store the distance between each planet and a common point: the sun.

# Start by adding the code to subtract first_planet from second_planet
# and store the result in a variable named distance_km. Display the value to the screen.

# Then add the code to convert distance_km to miles by dividing
# it by 1.609344 (the rough difference between miles and kilometers)
# and store the result in a variable named distance_mi. Display the value to the screen.

# Subtract these two values to determine the distance between the planets.
distance_km = second_planet - first_planet
print(distance_km)

