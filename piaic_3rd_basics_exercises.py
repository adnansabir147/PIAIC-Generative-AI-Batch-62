# Task 1: Simple Message
# Task:
# ● Assign a message to a variable.
# ● Print the message.
message = "Hello, this is a simple message."
print(message)

# Task 2: Simple Messages
# Task:
# ● Assign a message to a variable and print that message.
# ● Change the value of the variable to a new message, and print the new message.
message = "This is the first message."
print(message)
message = "This is the second message."
print(message)

# Task 3: Personal Message
# Task:
# ● Use a variable to represent a person’s name.
# ● Print a message to that person, such as, “Hello Eric, would you like to learn some Python today?”
person_name = "Eric"
print(f"Hello {person_name}, would you like to learn some Python today?")

# Task 4: Name Cases
# Task:
# ● Use a variable to represent a person’s name.
# ● Print the person’s name in lowercase, uppercase, and title case.
name = "Adnan Sabir"
print(name.lower())  # Lowercase
print(name.upper())  # Uppercase
print(name.title())  # Title Case

# Task 5: Famous Quote
# Task:
# ● Find a quote from a famous person you admire.
# ● Print the quote and the name of its author.
# The output should look something like the following:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(quote)

# Task 6: Famous Quote 2
# Task:
# ● Use a variable called famous_person to represent the famous person’s name.
# ● Compose the message and represent it with a variable called message.
# ● Print the message.
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

# Task 7: Stripping Names
# Task:
# ● Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# ● Print the name with the whitespace, then use lstrip(), rstrip(), and strip() to remove whitespace.
name_with_whitespace = "\t  Adnan Sabir\n"
print("Original:", name_with_whitespace)  # Original with whitespace
print("lstrip():", name_with_whitespace.lstrip())  # Leading whitespace removed
print("rstrip():", name_with_whitespace.rstrip())  # Trailing whitespace removed
print("strip():", name_with_whitespace.strip())  # All surrounding whitespace removed

# Task 8: Variable Sum
# Task:
# ● Assign the values 5, 10, and 15 to three variables x, y, and z.
# ● Print their sum.
x = 5
y = 10
z = 15
sum_result = x + y + z
print("Sum:", sum_result)

# Task 9: Variable Swap
# Task:
# ● Swap the values of two variables a and b.
# ● Print the values before and after the swap.
a = 10
b = 20
print("Before swap: a =", a, "b =", b)  # Before swapping
a, b = b, a
print("After swap: a =", a, "b =", b)  # After swapping

# Task 10: Favorite Color
# Task:
# ● Create a variable with your favorite color and print it.
# ● Then change the variable name and print again.
favorite_color = "Black"
print("Favorite color:", favorite_color)
fav_color = favorite_color
print("Favorite color (after renaming):", fav_color)

# Task 11: Changing Pet Name
# Task:
# ● Create a variable pet_name and set it to "Buddy".
# ● Change the value of pet_name to "Max" and print the new value.
pet_name = "Buddy"
print("Original pet name:", pet_name)
pet_name = "Max"
print("New pet name:", pet_name)

# Task 12: Observing Name Error
# Task:
# ● Assign the value "Sunshine" to a variable and print it.
# ● Then, mistakenly try to print a variable with a different name to observe the error.
sunshine = "Sunshine"
print(sunshine)
# Uncomment the following line to see the error:
# print(sunsine)  # This will raise a NameError because "sunsine" is not defined.

# Task 13: Reassigning Score
# Task:
# ● Assign the value 100 to a variable score and print it.
# ● Then assign a new value to score and print it again.
score = 100
print("Original score:", score)
score = 150
print("New score:", score)

# Task 14: City Name
# Task:
# ● Create a string variable city and assign it the name of a city you like.
# ● Print the city name.
city = "New York"
print("City name:", city)

# Task 15: Title Case Text
# Task:
# ● Create a variable text with the value "python programming" and print it in title case.
text = "python programming"
print("Title case:", text.title())

# Task 16: Lowercase Conversion
# Task:
# ● Assign a string with mixed cases to a variable and print it in all lowercase letters.
mixed_case_text = "PyTHon ProGRamming"
print("Lowercase:", mixed_case_text.lower())

# Task 17: Uppercase Conversion
# Task:
# ● Assign a string with mixed cases to a variable and print it in all uppercase letters.
mixed_case_text = "PyTHon ProGRamming"
print("Uppercase:", mixed_case_text.upper())

# Task 18: Current Temperature
# Task:
# ● Create a variable temperature with the value 25.
# ● Print "The current temperature is [temperature] degrees." using the variable.
temperature = 25
print(f"The current temperature is {temperature} degrees.")

# Task 19: Printing a Poem
# Task:
# ● Create a variable poem with a short poem that has multiple lines.
# ● Print the poem with each line starting on a new line.
poem = """The moonlight casts a silver veil,
On quiet seas, where dreams set sail.
Whispers float on the midnight air,
A gentle peace beyond compare."""
print(poem)