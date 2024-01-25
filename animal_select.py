from menu import Menu
from data import party_members
from utils import clear


animal_num = 3
def select_animals():
    selected_animals = []
    
    available_animals = party_members.copy()

    for i in range(animal_num):
        clear()
        party_menu = Menu(f"Who will go? ({i}/{animal_num})", available_animals)
        chosen_animal = party_menu.start_menu()
        selected_animals.append(chosen_animal.content)
        available_animals.remove(chosen_animal)

    clear()
    return selected_animals