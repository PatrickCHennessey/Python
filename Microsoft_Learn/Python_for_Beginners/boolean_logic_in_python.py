# if test_expression:
#     statement(s) to be run

# # Example
# a = 93
# b = 27
# if a >= b:
#     print(a)


# Output difference between indented print(b) line

# Example 1
# a = 24
# b = 44
# if a <= 0:
#     print(a)
# print(b)
# # Output is 44


# # Example 2
# a = 24
# b = 44
# if a <= 0:
#     print(a)
#     print(b)
# # Output is 0


# if test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run

# Example

# a = 27
# b = 93
# if a >= b:
#     print(a)
# else:
#     print(b)


# Use of elif

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run

# a = 27
# b = 93
# if a <= b:
#     print("a is less than or equal to b")
# elif a == b:
#     print("a is equal to b")


# Combine if, elif, and else

# if test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
# else:
#     # statement(s) to be run

# a = 27
# b = 93
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")


# Use of nested if, elif, and else

# if test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else:
#         # statement(s) to be run
# elif test_expression:
#     # statement(s) to be run
#     if test_expression:
#         # statement(s) to be run
#     else:
#         # statement(s) to be run
# else:
#     # statement(s) to be run


# Exercise

# You will start your project by creating the code to determine if a piece of space debris is of a dangerous size.
# For this exercise we will use an arbitrary size of 5 meters cubed (5m3);
# anything larger is a potentially dangerous object.

# In the cell below, add a variable named object_size and set it to 10 to represent 10m3.
# Then add an if statement to test if object_size is greater than 5.
# If it is, display a message saying We need to keep an eye on this object.
# Otherwise, display a message saying Object poses no threat.

# object_size = 10
# if object_size > 5:
#     print('We need to keep an eye on this object')
# else:
#     print('Object poses no threat')

# File complete