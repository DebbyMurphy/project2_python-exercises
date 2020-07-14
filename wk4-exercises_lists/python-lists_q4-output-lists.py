
# Ask the user to enter a string
# Split the string into a list, divided by spaces (hint: yourlist.split() will be useful).
# Convert the string to a list, where each character is an item inthe list (hint: list(yourlist) will be useful)
# For each list: output the length of the list, and the list itself. 

sentence = input("Enter a string: ")
# print(sentence)  

print()

words = sentence.split(" ")
# print(words)

characters = list(sentence)
# print(characters)

wordslength = (len(words))
characterslength = (len(characters))

print(f"{wordslength} {words}")
print(f"{characterslength} {characters}")

