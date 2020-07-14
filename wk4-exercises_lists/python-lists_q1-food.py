print("Week 4, Session 1 - Lists")

foods = [
    "orange", 
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1]) # This one is referencing the 6th item, which is a sublist, and the last item within that. 

