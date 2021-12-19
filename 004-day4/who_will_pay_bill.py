import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_items = len(names)

# example input
# Angela, Ben, Jenny, Michael, Chloe

randomInteger = random.randint(0, num_items-1)
#person_who_will_pay = random.choice(names)
print(f"{names[randomInteger]} is going to buy the meal today!")
