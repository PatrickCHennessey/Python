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