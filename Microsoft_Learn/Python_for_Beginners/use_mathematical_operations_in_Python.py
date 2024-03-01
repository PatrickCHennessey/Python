# # Addition
# add = 30 + 12
# print(add)

# # Subtraction
# difference = 30 - 12
# print(difference)

# # Multiplication
# product = 30 * 12
# print(product)

# # Division
# quotient = 30 / 12
# print(quotient)

# # Exercise convert 1042 seconds to minutes and seconds
# seconds = 1042
# display_minutes = seconds / 60
# print(display_minutes)

# # Output is 17.366666666667, but we want a non-decimal output.

# seconds = 1042
# display_minutes = seconds // 60 # a second forward slash will have the expression round down.
# print(display_minutes)

# Excellent now we know that 1042 divided by 60 = 17 minutes to find the remainder we incorporate the % modulo operator
# seconds = 1042
# display_seconds = 1042 % 60
# print(display_seconds)

# Converted the variables to a string to add "minutes" and "seconds" after both answers
# print(str(display_minutes) + ' minutes')
# print(str(display_seconds) + ' seconds')

# Let's explore how we can create a program that can calculate the distance between two planets. '
# We will start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).
# Note: Remove the commas when you're using the values.

# Start by creating two variables named first_planet and second_planet.
# Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.

# first_planet = 149597870
# second_planet = 778547200

# You have two variables which store the distance between each planet and a common point: the sun.

# Start by adding the code to subtract first_planet from second_planet
# and store the result in a variable named distance_km.

# Then add the code to convert distance_km to miles by dividing
# it by 1.609344 (the rough difference between miles and kilometers)
# and store the result in a variable named distance_mi. Display the value to the screen.

# Subtract these two values to determine the distance between the planets.
# distance_km = second_planet - first_planet
# print(distance_km)
# # 628949330
#
# # Add the code to convert distance_km to miles by dividing it by 1.609344
# # (the rough difference between miles and kilometers), and store it in a variable named distance_mi

# distance_mi = distance_km / 1.609344
# print(distance_mi)
# # 390810995.0389724

# Exercise: Create an application to work with numbers and user input

# We want to read the distance from the sun for two planets, and then display the distance between the planets.
# We'll do this by using input to read the values, int to convert to integer,
# and then abs to convert the result into its absolute value.

# Start by adding the code to prompt the user for the distance between the sun and the first planet,
# and then the second. Store each result in variables named first_planet_input and second_planet_input.

first_planet_input = input('Enter the distance from the sun for the first planet in km')
second_planet_input = input('Enter the distance from the sun for the second planet in km')

# Because input returns string values, we need to convert them to numbers.
# Add the code to convert each input into an integer using int.
# Store the values in first_planet and second_planet respectively.

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

print(first_planet)
print(second_planet)

# With your values stored as numbers, you can now add the code to perform the calculation,
# subtracting the first planet from the second. Because the second planet might be a greater number,
# you'll use abs to convert it to an absolute value. Subtract first_planet from second_planet and
# convert the result to its absolute value by using abs. Store the result in a variable named distance_km.
# Then display the result on the screen.

distance_km = abs(second_planet-first_planet)
print(distance_km)

# Completed use_mathematical_operations_in_Python.py file
