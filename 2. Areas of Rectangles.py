                                                                           # Code made by Frank Lochtenberg
print("Hello user!")                                                       # Hello

print("What I want from you is the length and width of two rectangles.")   # Introduction sentence

length_1 = int(input("The length of rectangle 1:"))                        # Asks the user for the length and width of two rectangles
width_1 = int(input("The width of rectangle 1:"))
length_2 = int(input("The length of rectangle 2:"))
width_2 = int(input("The width of rectangle 2:"))

rectangle_1 = length_1 * width_1                                           # Calculates the areas of the two areas
rectangle_2 = length_2 * width_2

if rectangle_1 >= rectangle_2:                                             # Checks which area is bigger
   print("The area of rectangle 1 is greater than rectangele 2.")          # Then prints the result
if rectangle_1 == rectangle_2:
   print("The areas of both rectangles are the same.")
if rectangle_1 <= rectangle_2:
   print("The area of rectangle 2 is greater than rectangle 1.")

print("Goodbye user!")                                                     # Goodbye
