                                                                             # Code made by Frank Lochtenberg
print("Hello user!")                                                         # Hello

print("Is anyone in your party a vegetarian?")                               # Asks if anyone in the party is:
v = int(input("press 1 for yes, 2 for no:"))                                 # - Vegetarian
print("Is anyone in your party a vegan?")                                    # - Vegan
g = int(input("press 1 for yes, 2 for no:"))                                 # - Gluten-free
print("Is anyone in your party gluten free?")                                 
f = int(input("press 1 for yes, 2 for no:"))

print("These are your restaurant options:")                                  # Result Introduction Sentence

if v == 2 and g == 2 and f == 2:                                             # Checks which restaurant corresponds to the users needs
    print("Joe's Gourmet Burgers")
if (v == 1 or v == 2) and g == 2 and (f == 1 or f == 2):
    print("Main Street Pizza Company")
if (v == 1 or v == 2) and (g == 1 or g == 2) and (f == 1 or f == 2):
    print("Corner Café")
if (v == 1 or v == 2) and g == 2 and f == 2:
    print("Mama's Fine Italian")
if (v == 1 or v == 2) and (g == 1 or g == 2) and (f == 1 or f == 2):
    print("The Chef's Kitchen")
if (v < 1 or v > 2) or (g < 1 or g > 2) or (f < 1 or f > 2):
    print("You pressed the wrong button to one or more of the questions!")

print("Goodbye user!")                                                       # Goodbye
