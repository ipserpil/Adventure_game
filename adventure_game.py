import time
import random
import sys


def print_sleep(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")


def intro():
    print_sleep("After a full day of trekking in the mountain "
                "with your friends, you find yourself alone in tent.")
    print_sleep("You have no idea where everybody has gone.")
    print_sleep("The peace quickly fades when you hear "
                "a grotesque sound behind your tent.")
    print_sleep("Is it a bear or is it something else?!")
    print_sleep("You have to decide:")


def first_decision():
    while True:
        decision = input("Enter A to get out of the tent.\n"
                         "Enter B to stay inside the tent.\n").lower()
        if decision == "a":
            get_outside()
            break
        elif decision == "b":
            print_sleep("You try to stay quiet.")
            print_sleep("After some time your tent started shaking"
                        "...and get more scared.")
            stay_inside()
            break
        else:
            print_sleep("Sorry! I don't understand. Please input A or B.")


def get_outside():
    print_sleep("You are outside now.")
    animals = ["bear", "squirrel", "wild boar", "deer"]
    animal = random.choice(animals)
    print_sleep(f"You can barely see in the darkness...it is a {animal}.")
    print_sleep("What do you do next?")
    while True:
        first_action = input("1. Run quickly into the Cabin\n"
                             f"2. Ask {animal} go away\n"
                             f"3. Beat the {animal}\n")
        if first_action == "1":
            to_cabin()
            break
        elif first_action == "2":
            shoo(animal)
            break
        elif first_action == "3":
            beat_animal(animal)
            break
        else:
            print_sleep("Sorry! I don't understand. Please choose:")


def stay_inside():
    while True:
        think_again = input("Enter 1 to get out of the tent.\n"
                            "Enter 2 to stay inside the tent.\n")
        if think_again == "1":
            get_outside()
            break
        elif think_again == "2":
            print_sleep("You already tried this. "
                        "It seems like it is not a good idea.")
        else:
            print_sleep("Sorry! I don't understand. Please choose:")


def to_cabin():
    print_sleep("You are safe now!")
    play_again()


def shoo(animal):
    print_sleep("SHOO! SHOO!")
    animal_reactions = random.choice([f"The {animal} leaves",
                                      f"The {animal} ignores you"])
    if animal_reactions == f"The {animal} leaves":
        print_sleep("Whoo! You are safe now!")
    else:
        print_sleep(f"The {animal} ignores you.")
        while True:
            second_action = input(f"1. Beat the {animal}\n"
                                  "2. Do nothing\n")
            if second_action == "1":
                if animal == "bear":
                    print_sleep("You lost!")
                    break
                elif animal == "squirrel":
                    print_sleep("You won!")
                    break
                elif animal == "wild boar":
                    print_sleep("You lost!")
                    break
                elif animal == "deer":
                    print_sleep("You won!")
                    break
                else:
                    print_sleep("Sorry! I don't understand.")
            elif second_action == "2":
                print_sleep("You lost!")
                break
            else:
                print_sleep("Sorry! I don't understand.")
    play_again()


def beat_animal(animal):
    while True:
        if animal == "bear":
            print_sleep("You lost!")
            break
        elif animal == "squirrel":
            print_sleep("You won!")
            break
        elif animal == "wild boar":
            print_sleep("You lost!")
            break
        elif animal == "deer":
            print_sleep("You won!")
            break
        else:
            print_sleep("Sorry! I don't understand")
    play_again()


def play_again():
    while True:
        again = input("Would you like to play again Bambilici? (y/n)").lower()
        if again == "y":
            intro()
            first_decision()
            break
        elif again == "n":
            print_sleep("Bye Bye! See you next time!")
            break
        else:
            print_sleep("Sorry! I don't understand.")


def adventure_game():
    name = input("What is your name?\n")
    if len(name) >= 2:
        print_sleep(f"Welcome to Bambilici, {name}!")
        intro()
        first_decision()
    elif len(name) == 0:
        print_sleep("Please enter name.")
        adventure_game()
    else:
        print_sleep("Name too short. Please try again.")
        adventure_game()


adventure_game()
