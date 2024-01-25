from combat import Combat
import data
from animal_select import select_animals
from time import sleep
from menu import Menu, MenuOption
from utils import clear
import utils
from numpy import clip


#Prints introduction text
def play_intro():
    for text in data.intro_text:
        print(text)
        sleep(5)


#Main game function
def play_game():
    play_intro()

    combat = Combat()

    party = select_animals()

    for animal in party:
        combat.add_battler(animal)

    data.starting_room.enter(combat)


#Changes text speed in combat
def change_text_speed():
    print("Enter New Text Speed in Seconds (0.2 - 6) (Default 1.5)")
    global text_speed
    new_speed = 0.0
    while True:
        try:
            new_speed = float(input(":"))
            break
        except:
            continue
    new_speed = clip(new_speed, 0.2, 6)
    utils.text_speed = new_speed
    print("New Speed Is", utils.text_speed)
    sleep(utils.text_speed)


def main():
    print("Please Maximise Console")
    sleep(1)
    clear()

    main_menu = Menu(
        data.title_text, [
            MenuOption("Play", 0),
            MenuOption("How To Play", 1),
            MenuOption("Change Battle Text Speed", 2),
            MenuOption("Quit", 3)
        ])

    while True:
        option = main_menu.start_menu()

        if option.content == 0:
            clear()
            play_game()

            sleep(4)
            clear()
        elif option.content == 1:
            print(data.rules)
            input("Press Enter When Done")
            clear()
        elif option.content == 2:
            change_text_speed()
            clear()
        elif option.content == 3:
            print("...")
            break


if __name__ == "__main__":
    main()
