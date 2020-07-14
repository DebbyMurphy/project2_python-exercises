

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

# there are 5 sublists, within the list
# each sublist contains name + email
# I need to grab the first item of each sublist, insert a colon + space, then pull through the second (or last) item of the sublist. 
# I need to do this, for each sublist - over and over. Use a For Loop. 

print()






for customer in mailing_list:
    print(f"{customer[0]}: {customer[1]}")







# # name = mailing_list[0]
# # email = mailing_list[1]

# # for mailing_list
# #     print(f"{name}: {email}")


# # name = mailing_list[0]
# # email = mailing_list[1]

# for value in mailing_list:
#     print(f"{value[0]}: {value[1]}")


# print()

# name = (mailing_list[0][0])
# email = (mailing_list[0][1])
# for customers in mailing_list:
#     print(f"{name}: {email}")


# print()

# list = [["John Doe", 40], ["Jane Doe", 38],["Joe Bloggs", 34]]

# for elemento in list:
#     print("Name: " + str(elemento[0]))
#     print("Age: " + str(elemento[1]))
#     print(" - - -  - - -  - - -  - - -  - - -  - - -  - - - ")


# print()

# # for value in mailing_list:
# #     print(value)


# # # for name in mailing_list:
# # #     print(f"{name[0]}: ")
# # # for email in mailing_list:
# # #     print(email[1])
# # for mailing_list:
# #     print(f"{name[0]}: {email[1]}")

# print()


# count =0
# while count<1:
#   print(mailing_list[count])
#   count+=1

# # tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]

# # print(tea_collection)

# # print(tea_collection[0])
# # print(tea_collection[3])
# # print(tea_collection[0:2])