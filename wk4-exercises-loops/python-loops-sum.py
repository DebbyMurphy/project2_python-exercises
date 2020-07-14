

# # -------------------------------------------------------------

# num_int = None
# # num_sum = 0

# while num_int != False:
#     num_str = input("Enter a number: ")
#     num_int = int(num_str)
#     if num_int > True:
#         continue
#     # else:
#     #     print(sum(num_int)          # NEARLY WORKING

# ---------------------------------------------------------------------


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

