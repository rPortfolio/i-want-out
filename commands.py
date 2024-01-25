#Commands that handle health modification such as attacking or healing
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


class Command(ABC):
    """Command base class from which all other commands inherit"""
    @abstractmethod
    def execute(self):
        pass


class Attack(Command):
    """Deducts user's power from the enemy's hp"""
    def __init__(self, target, user):
        self.target = target
        self.user = user

    def execute(self):
        damage = self.user.pwr
        self.target.harm(damage)


class ChanceAttack(Attack):
    """Has a 40% chance of hitting for 3x damage"""
    def __init__(self, target, user):
        self.target = target
        self.user = user
        super().__init__(target, user)
    
    def execute(self):
        random_number = randint(0, 10)
        if random_number >= 4:
            return
        
        for i in range(3):
            super().execute()


class DoubleAttack(Attack):
    """Deducts user's power from the enemy's hp but costs user's hp"""
    def __init__(self, target, user):
        self.target = target
        self.user = user
        super().__init__(target, user)

    def execute(self):
        super().execute()
        super().execute()
        self.user.harm(int(self.user.pwr/2))


class SpeedAttack(Attack):
    """Deducts user's speed from the enemy's hp; Costs user's speed"""
    def execute(self):
        damage = self.user.spd
        self.target.harm(damage)
        self.user.spd -= 3
        if self.user.spd < 0:
            self.user.spd = 0


class Recover(Command):
    def __init__(self, target, user):
        self.target = target
        self.recovery = user.rpwr

    def execute(self):
        self.target.recover(self.recovery)


@dataclass
class Action:
    """Contains information on who an action targets"""
    targets_enemies:bool
    targets_all:bool
    command:Command