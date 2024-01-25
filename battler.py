from dataclasses import dataclass


@dataclass
class Battler:
    """Stores and handles information about battlers"""
    name:str
    is_animal:bool
    hp:int
    spd:int
    pwr:int
    rpwr:int
    actions:list

    def harm(self, amt):
        self.hp -= amt

    def recover(self, amt):
        self.hp += amt
