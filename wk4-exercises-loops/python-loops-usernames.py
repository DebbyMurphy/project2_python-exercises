

output_numbered_list = False

number_list = []
while output_numbered_list == False:
    number = input("Enter a number: ")
    if number == "":
        output_numbered_list = True
    else:
        number_list.append(int(number))
print(number_list)

total = sum(number_list)
print(total)





nameslist = []

firstname = input("Hi, what's your first name?! ")
middlename = input(f"Cool, hey {firstname} what about your middle name? ")
lastname = input(f"Thanks. And finally - please enter your last name: ")

nameslist.insert(0, firstname)
nameslist.insert(1, middlename)
nameslist.insert(2, lastname)

print(nameslist)




# I have a blank list
nameslist = []
# I need to fill that list with names
# Ask user for a name three times, using a while loop 
while names in nameslist < 3:
    name = input("Enter name: ")

# Stop asking for names when you have three names (while names < 3)

# Once you have three names - append the names into the previously blank list 

# Print that list to see what it looks like, this is not the final output. 

# Final output = access each of those names in the list, using a for loop 

# No break required because it's a for loop and there are only three names 

# print a list of those names


