# fact = "The Moon has no atmosphere."
# print(fact)
# # Output: "The Moon has no atmosphere."

# fact = "The Moon has no atmosphere."
# fact + "No sound can be heard on the Moon."
# print(fact)
# # Output: The Moon has no atmosphere.
# # Since the second statement is not defined in the fact variable, it is not included in the output

# fact = "The Moon has no atmosphere."
# two_facts = fact + "No sound can be heard on the Moon."
# print(two_facts)
# # Output: The Moon has no atmosphere. No sound can be heard on the Moon.

# multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
# print(multiline)
# # \n will indicate that the following string will continue on the next line.

# heading = "temperatures and facts about the moon"
# heading_upper = heading.title()
# print(heading_upper)
# # Output: Temperatures And Facts About The Moon

# temperatures = "Daylight: 260 F Nighttime: -280 F"
# temperatures_list = temperatures.split()
# print(temperatures_list)
# # Resulting output ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']

# temperatures = "Daylight: 260 F\n Nighttime: -280 F"
# temperatures_list = temperatures.split('\n')
# print(temperatures_list)
# # Defining split('\n') will tell the script to split when it encounters \n.
# # The resulting output is then ['Daylight: 260 F', 'Nighttime: -280 F']

# print("Moon" in "This text will describe facts and challenges with space travel")
# # Output: False
# # As Moon is not contained in string

# print("Moon" in "This text will describe facts about the Moon")
# # Output: True
# # As Moon is contained in string

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Moon"))
# # Output: -1
# # -1 indicates when a word is not found in string.

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Mars"))
# # Output: 64, which is the position Mars appears in the string.

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.count("Mars"))
# print(temperatures.count("Moon"))
# # Output:
# # 1
# # 0
# # .count() indicates how many times the designated item occurs in the string.

# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(':')
# print(parts)
# print(parts[1])
# # Output: ['Mars average temperature', ' -60 C']
# # ' -60 C'
# # -1 in this example returns the last item. 0 would return Mars Average Temperature. 1 would return -60 C

# Exercise:

# Step 1: Store the following paragraph as a variable called text.

# Interesting facts about the Moon. The Moon is Earth's only satellite.
# There are several interesting facts about the Moon and how it affects life here on Earth.
# On average, the Moon moves 4cm away from the Earth every year.
# This yearly drift is not significant enough to cause immediate effects on Earth.
# The highest daylight temperature of the Moon is 127 C.

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
print(text)

# Step 2: Separate the paragraph into sentences

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split('.')
print(sentences)

# Step 3: Have script find any sentences that mention tempperature.
# Have the code to loop through the sentences variable. For each sentence, search for the word temperature.
# If the word is found, print the sentence.

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)

