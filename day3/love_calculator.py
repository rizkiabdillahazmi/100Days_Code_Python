print("Welcome to the Love Calculator")
name1 = input("What is Your Name? \n")
name2 = input("What is Their Name? \n")

name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

true_t = name.count("t")
true_r = name.count("r")
true_u = name.count("u")
true_e = name.count("e")
total_true = true_t + true_r + true_u + true_e

love_l = name.count("l")
love_o = name.count("o")
love_v = name.count("v")
love_e = name.count("e")
total_love = love_l + love_o + love_v + love_e

print(f"T occurs {true_t} times")
print(f"R occurs {true_r} times")
print(f"U occurs {true_u} times")
print(f"E occurs {true_e} times")
print(f"Total = {total_true} \n")

print(f"L occurs {love_l} times")
print(f"O occurs {love_o} times")
print(f"V occurs {love_v} times")
print(f"E occurs {love_e} times")
print(f"Total = {total_love} \n")

love_score = int(str(total_true) + str(total_love))

if (love_score <= 10) or (love_score >= 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")
