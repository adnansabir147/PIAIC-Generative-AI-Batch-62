# Exercise 3-1: Names
# Task: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ["Alice", "Bob", "Charlie", "David"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Exercise 3-2: Greetings
# Task: Start with the list you used in Exercise 3-1. Instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
greeting = "Hello"
print(f"{greeting}, {names[0]}!")
print(f"{greeting}, {names[1]}!")
print(f"{greeting}, {names[2]}!")
print(f"{greeting}, {names[3]}!")

# Exercise 3-3: Your Own List
# Task: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."
modes_of_transport = ["car", "bicycle", "motorcycle"]
print(f"I would like to own a Tesla {modes_of_transport[0]}.")
print(f"I enjoy riding my {modes_of_transport[1]}.")
print(f"I would love to try a Harley-Davidson {modes_of_transport[2]}.")

# Exercise 3-4: Guest List
# Task: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest_list = ["Albert Einstein", "Marie Curie", "Isaac Newton"]
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")

# Exercise 3-5: Changing Guest List
# Task: Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. Print a second set of invitation messages, one for each person who is still in your list.
print(f"Unfortunately, {guest_list[1]} can't make it.")
guest_list[1] = "Nikola Tesla"
print(f"Dear {guest_list[0]}, you are still invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are still invited to dinner.")

# Exercise 3-6: More Guests
# Task: Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table. Use insert() to add one new guest to the beginning of your list. Use insert() to add one new guest to the middle of your list. Use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.
print("Great news! We found a bigger table, so more guests can be invited!")
guest_list.insert(0, "Galileo Galilei")
guest_list.insert(2, "Leonardo da Vinci")
guest_list.append("Stephen Hawking")
print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are still invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are still invited to dinner.")
print(f"Dear {guest_list[4]}, you are still invited to dinner.")
print(f"Dear {guest_list[5]}, you are invited to dinner.")

# Exercise 3-7: Shrinking Guest List
# Task: Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. Print a message to each of the two people still on your list, letting them know they’re still invited. Use del to remove the last two n...
print("Sorry, but we can only invite two people for dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, we can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, we can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, we can't invite you to dinner.")
uninvited_guest = guest_list.pop()
print(f"Sorry {uninvited_guest}, we can't invite you to dinner.")
print(f"{guest_list[0]} and {guest_list[1]}, you are still invited.")
del guest_list[1]
del guest_list[0]
print("Final guest list:", guest_list)

# Exercise 3-8: Seeing the World
# Task: Think of at least five places in the world you’d like to visit. Store the locations in a list. Make sure the list is not in alphabetical order. Print your list in its original order. Use sorted() to print your list in alphabetical order without modifying the actual list. Show that your list is still in its original order by printing it. Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. Show that your list is still in its original order ...
places_to_visit = ["Tokyo", "New York", "Paris", "Sydney", "Cape Town"]
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# Exercise 3-9: Every Function
# Task: Write a program that creates a list containing items (like mountains, rivers, countries, etc.) and then uses each function introduced in this chapter at least once.
mountains = ["Everest", "K2", "Kilimanjaro", "Denali"]

# Using append()
mountains.append("Aconcagua")
print(mountains)

# Using insert()
mountains.insert(2, "Elbrus")
print(mountains)

# Using pop()
removed_mountain = mountains.pop()
print(f"Removed mountain: {removed_mountain}")
print(mountains)

# Using del
del mountains[1]
print(mountains)

# Using sort()
mountains.sort()
print(mountains)

# Using reverse()
mountains.reverse()
print(mountains)

# Using sorted()
print(sorted(mountains))

# Exercise 3-10: Intentional Error
# Task: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.
print(mountains[10])  # Intentional index error
