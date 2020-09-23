                                                                                           # Code made by Frank Lochtenberg
print("Hello user!")                                                                       # Hello

print("I see that you have trouble with the Wi-Fi.")                                       # Introduction sentences
print("Here are some tips.")

print("Reboot the computer and try to connect.")                                           # Gives the user a tip and asks if it helped
print("Did that fix the problem?")                                                         # If yes then goodbye
a = int(input("press 1 for no, press 2 for yes."))                                         # If no another tip                                  
if a == 1:                                                                                 # Max of 5 tips
    print("Reboot the router and try to connect.")                                            
    print("Did that fix the problem?")
    b = int(input("press 1 for no, press 2 for yes."))
    if b == 1:
        print("Make sure the cables between the router & modem are plugged in firmly.")
        print("Did that fix the problem?")
        c = int(input("press 1 for no, press 2 for yes."))
        if c == 1:
            print("Move the router to a new location and try to connect.")
            print("Did that fix the problem?")
            d = int(input("press 1 for no, press 2 for yes."))
            if d == 1:
                print("Get a new router.")
                print("Have a nice day and goodbye!")
            if d == 2:
                print("Have a nice day and goodbye!")
        if c == 2:
            print("Have a nice day and goodbye!")
    if b == 2:
         print("Have a nice day and goodbye!")
if a == 2:
    print("Have a nice day and goodbye!")

