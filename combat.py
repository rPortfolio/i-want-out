from random import choice
from menu import MenuOption, Menu
from time import sleep
from utils import clear
import utils
from copy import deepcopy

class TurnQueue:
    """Class which keeps track of order of battlers"""
    _current_battler:object
    
    def __init__(self, battlers):
        self._battlers = battlers

    def sort_speed(self, e):
        return e.spd
    
    def reset(self):
        self._battlers.sort(key = self.sort_speed, reverse = True)
        self._current_battler = self._battlers[0]
    
    def advance_battler(self):
        current_battler_index = self._battlers.index(self._current_battler)
        if current_battler_index == len(self._battlers) - 1:
            self._current_battler = self._battlers[0]
        else:
            self._current_battler = self._battlers[current_battler_index + 1]

    def get_current_battler(self):
        return self._current_battler


class TurnController:
    """Handles logic during a party member's turn"""
    def __init__(self, _battlers):
        self._battlers = _battlers

    def turn_text(self, battler, action, target):
        print(f"{battler} does a(n) {action} on {target}")

    #Returns list of available targets
    def get_target_options(self, battlers, targets_enemies):
        possible_targets = [x for x in battlers if x.is_animal != targets_enemies]
        target_options = []
        for target in possible_targets:
            new_target_option = MenuOption(target.name, target)
            target_options.append(new_target_option)
        return target_options

    #Handles input and execution of a party members turn
    def play_party_turn(self, current_battler):
        action_menu = Menu(f"{current_battler.name}'s Turn", current_battler.actions)
        action_choice = action_menu.start_menu()
        action = action_choice.content

        targets = self.get_target_options(self._battlers, action.targets_enemies)

        if action.targets_all:
            self.turn_text(current_battler.name, action_choice.name, "all")
            for target in targets:
                turn = action.command(target.content, current_battler)
                turn.execute()
            return
        
        target_menu = Menu("Select Target", targets)
        target = target_menu.start_menu().content
        
        turn = action.command(target, current_battler)
        turn.execute()
        self.turn_text(current_battler.name, action_choice.name, target.name)

    #Handles selection and execution of an enemy's turn
    def play_enemy_turn(self, current_battler):
        action_choice = choice(current_battler.actions)
        action = action_choice.content
        targets = self.get_target_options(self._battlers, not action.targets_enemies)

        if action.targets_all:
            self.turn_text(current_battler.name, action_choice.name, "all")
            for target in targets:
                turn = action.command(target.content, current_battler)
                turn.execute()
            return

        target = choice(targets).content
        
        turn = action.command(target, current_battler)
        turn.execute()
        self.turn_text(current_battler.name, action_choice.name, target.name)
        


class Combat:
    """Handles logic during battle"""
    _battlers = []
    
    turn_queue = TurnQueue(_battlers)
    turn_controller = TurnController(_battlers)

    #Returns list of enemies
    def get_enemy_battlers(self):
        return [x for x in self._battlers if not x.is_animal]

    #Returns list of players
    def get_party_battlers(self):
        return [x for x in self._battlers if x.is_animal]

    #Print name and health of ever battler
    def print_battle_stats(self):
        print("ENEMIES:")
        for battler in self.get_enemy_battlers():
            print(" ", battler.name, " (HP: ", battler.hp, ")")
        print("ANIMALS:")
        for battler in self.get_party_battlers():
            print(" ", battler.name, " (HP: ", battler.hp, ")")
        print()

    #Adds a copy of the
    def add_battler(self, battler):
        self._battlers.append(deepcopy(battler))

    #Removes battlers with an hp less than zero excluding current_battler
    def remove_inactive_battlers(self, current_battler):
        for battler in self._battlers:
            if battler.hp <= 0 and battler is not current_battler:
                self._battlers.remove(battler)
        
    #Main battle function.  Returns true if the battle is won and false if the battle is lost
    def start_battle(self):
        print("Foes Approach!")
        sleep(utils.text_speed)
        self.turn_queue.reset()
        
        won = False
        
        while True:
            clear()
            
            self.print_battle_stats()
            current_battler = self.turn_queue.get_current_battler()

            #Checks if the battle was won or lost based on if there are any enemies or players still active
            if not self.get_enemy_battlers():
                won = True
                break
            elif not self.get_party_battlers():
                won = False
                break
            
            sleep(utils.text_speed)
            
            if current_battler.is_animal:
                self.turn_controller.play_party_turn(current_battler)
            else:
                self.turn_controller.play_enemy_turn(current_battler)

            self.remove_inactive_battlers(current_battler)
            self.turn_queue.advance_battler()
            #Current Battler needs to be removed separately or else the turn queue will break
            if current_battler.hp <= 0:
                self._battlers.remove(current_battler)
            sleep(utils.text_speed)
        sleep(utils.text_speed)
        if won:
            clear()
            print("You won!\n")
        else:
            print("You were defeated!")
        sleep(utils.text_speed)
        return won
