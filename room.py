from menu import Menu, MenuOption
from utils import clear

class Room:
    """Contains information for an area of the game.
    Includes enemy encounters and other rooms."""
    def __init__(self, name, connected_rooms, text, encounter):
        self.name = name
        self.connected_rooms = connected_rooms
        self.text = text
        self.encounter = encounter

    def enter(self, combat):
        if self.encounter:
            for enemy in self.encounter:
                combat.add_battler(enemy)
            won = combat.start_battle()
            if not won:
                return

        room_options = []
        if self.connected_rooms:
            for room in self.connected_rooms:
                new_room_option = MenuOption(room.name, room)
                room_options.append(new_room_option)
        
            progress_menu = Menu(self.text, room_options)
            next_room = progress_menu.start_menu().content
            clear()
            next_room.enter(combat)
        else:
            print("You Escaped!")