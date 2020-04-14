import time
import random

characters = ["Politician", "Policeman", "Minister", "A Tiny Laura"]
character = random.choice(characters)


def print_pause(string):
    print(string)
    time.sleep(2)


def intro():
    print_pause("You have Landed in the mysterious land of Durban")
    print("You are here to vanquish a corrupt", character)
    time.sleep(2)
    print_pause("Infront of you is a newly built house \n"
                "on the right is a brand new car")
    print_pause("In your hand you have your trusty subpoena")


def option_one(items):
    print_pause("You approach the house")
    print_pause("Suddenly a giant bodygaurd steps in your way")
    if "evidence" in items:
        print_pause("The body gaurd see's the incriminating evidence"
                    "in our hand and asks to turn witness")
        print_pause(f"You enter the house where you find the {character}")
        print_pause("they see the evidence and turn themselves in")
        print_pause(f" Congrats, you have cought the corrupt {character}")
        print_pause("would you like to play again?")
        play_again()
    else:
        fight(items)


def fight(items):
    print_pause("You can choose to fight the bodygaurd"
                " or come back with more evidence")
    fight_bodygaurd = input("Press 1 to fight the bodygaurd"
                            " or 2 to run away\n")
    if fight_bodygaurd == "1":
        print_pause("You are no match for the bodygaurd"
                    "and have been defeated")
        print_pause("would you like to play again")
        play_again()
    elif fight_bodygaurd == "2":
        print_pause("You have run away, great choice")
        options(items)


def option_two(items):
    print_pause("You open up the car")
    if "evidence" in items:
        print_pause("Nothing left here to find")
        print_pause("you decide to go back to where you started")
        options(items)
    else:
        print_pause("Oh wait what is this,"
                    "it looks like a ledger of illegal activities")
        items.append("evidence")
        print_pause("You leave the car with the evidence,"
                    "and head back to where you started")
        options(items)


def options(items):
    option = input("Press 1 to knock on the door to the house \n"
                   "Press 2 to search the car\n")
    if option == "1":
        option_one(items)
    elif option == "2":
        option_two(items)
    else:
        print_pause("You must select either 1 or 2")
        options(items)


def play_again():
    while True:
        play = input("Press Y to play again or N to exit\n").lower()
        if "y" in play:
            print_pause("Rock n roll buddy, lets play again")
            the_game()
        elif "n" in play:
            print_pause("Thanks for playing")
            break
        else:
            play_again()
        break


def the_game():
    items = []
    intro()
    options(items)


the_game()
