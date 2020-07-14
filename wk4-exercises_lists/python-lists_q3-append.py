# Q3) Ask the user for three names, append them to a list, then print the list.

# Input
# Izzy
# Archie
# Boston

# Output
# ["Izzy", "archie", "Boston"]


nameslist = []

firstname = input("Hi, what's your first name?! ")
middlename = input(f"Cool, hey {firstname} what about your middle name? ")
lastname = input(f"Thanks. And finally - please enter your last name: ")

nameslist.insert(0, firstname)
nameslist.insert(1, middlename)
nameslist.insert(2, lastname)

print(nameslist)



