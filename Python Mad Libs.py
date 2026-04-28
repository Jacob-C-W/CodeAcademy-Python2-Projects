"""
Description: Madlibs.py is an interactive adlibs story using python
"""

# The template for the story

STORY = "This morning _ woke up feeling _. 'It is going to be a _ day!' Outside, a bunch of _s were protesting to keep _ in stores. They began to _ to the rhythm of the _, which made all the _s very _. Concerned, _ texted _, who flew _ to _ and dropped _ in a puddle of frozen _. _ woke up in the year _, in a world where _s ruled the world."

print "madlibs_project.py has started."

print "now please provide a name."
nam1 = raw_input("Enter a name: ")

print "now please provide an adjective."
adj1 = raw_input("Enter an adjective: ")
print "now please provide another adjective."
adj2 = raw_input("Enter an adjective: ")
print "now please the provide the last adjective."
adj3 = raw_input("Enter an adjective: ")

print "now please provide a verb"
ver1 = raw_input("Enter a verb: ")

print "now please provide a noun"
nou1 = raw_input("Enter a noun: ")
print "now please provide another noun"
nou2 = raw_input("Enter a noun: ")

print "now please provide an animal"
ani1 = raw_input("Enter a animal: ")

print "now please provide a food"
foo1 = raw_input("Enter a food: ")

print "now please provide a fruit"
fru1 = raw_input("Enter a fruit: ")

print "now please provide a superhero"
sup1 = raw_input("Enter a superhero: ")

print "now please provide a country"
cou1 = raw_input("Enter a country: ")

print "now please provide a dessert"
des1 = raw_input("Enter a dessert: ")

print "now please provide a year"
yea1 = raw_input("Enter a year: ")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." \
 % (nam1, adj1, adj2, ani1, foo1, ver1, nou1, fru1, adj3, nam1, sup1, nam1, cou1, nam1, des1, nam1, yea1, nou2)

print STORY

# print "now please provide a X"
# X = raw_input("Enter a X: ")
