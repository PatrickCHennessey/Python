#  Project Goals: Band Name Generator
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:

# 1. Create a greeting for the program
greeting = ("Hello! Welcome to the band name generator program."
            "\nIn order to create a rocking *pause for groans* band name, we'll need some additional information.")
print(greeting)

# 2. Ask the user for the city that they grew up in.
city_name = input("Question #1: What city did you grow up in? ""\n")
print(city_name + ", Right on! That's a great city!")

# 3. Ask the user for the name of a pet.
name_of_pet = input("Question #2: What is the name of your pet(s) ""\n")
print(name_of_pet + ", Right on! That's a great pet name!")

# 4. Combine the name of their city and pet and show them their band name.
print("Now based off of the information you entered it's time to generate a rad band name for your group. \n"
      "Generating...\n"
      "Generating...\n"
      "Okay your new rocking band name is")

generated_band_name = ("(The) " + city_name + " " + name_of_pet + "(s)")
print(generated_band_name)

# 5. Make sure the input cursor shows on a new line: