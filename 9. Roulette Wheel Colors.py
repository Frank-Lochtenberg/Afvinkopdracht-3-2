                                                          # Code made by Frank Lochtenberg
print("Hello user!")

n = int(input("What is your pocket number!"))             # Asks user for a pocket number

while n < 0 or n > 36:                                    # Checks which the pocket number belongs
    print("The pocket number is invalid!")                # Then prints the result
    n = int(input("Please pick a new pocket number:"))
if n == 0:
    print("The pocket color is Green.")
if (n % 2) == 0 and n <= 10 and n >= 1:
    print("The pocket color is Black.")
if (n % 2) != 0 and n <= 10 and n >= 1:
    print("The pocket color is Red.")
if (n % 2) == 0 and n <= 18 and n >= 11:
    print("The pocket color is Red.")
if (n % 2) != 0 and n <= 18 and n >= 11:
    print("The pocket color is Black.")
if (n % 2) == 0 and n <= 28 and n >= 19:
    print("The pocket color is Black.")
if (n % 2) != 0 and n <= 28 and n >= 19:
    print("The pocket color is Red.")
if (n % 2) == 0 and n <= 36 and n >= 29:
    print("The pocket color is Red.")
if (n % 2) != 0 and n <= 36 and n >= 29:
    print("The pocket color is Black.")

print("Goodbye user!")                                    # Goodbye
