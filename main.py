from art import logo
from BlackJack_Brain import BlackJack

# Final step will involve finalizing shuffle method by collecting a list of all cards currentl in play and removing them from the reinitialized deck

print(logo)
print("Created by Quillborn\n")
print("Welcome to Black Jack!")

BlackJack()
restart = input("Would you like to start a new game? Y/N :")
while True:   
    if restart == "y":
        BlackJack()
    elif restart == "n":
        print("Thanks for playing BlackJack! ")
        break
    else:
        print('Invalid input. Please select "y" or "n".')

exit()