# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

nl10 = "Ruud Gullit"
nl12 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = nl10 + " " + str(goal_0) + ", " + nl12 + " " + str(goal_1)
print(scorers)

report =  f"{nl10} scored in the {goal_0}nd minute\n{nl12} scored in the {goal_1}th minute"
print(report)

player = nl10

first_name = nl10[:nl10.find(" ")]
print("*" + first_name + "*")

last_name = nl10[nl10.find(" ") + 1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = first_name[0] + ". " + last_name
print(name_short)

chant = (f"{first_name}! " * len(first_name))[0:-1]
print(chant)

good_chant = (chant[-1] != " ")
print(good_chant)
