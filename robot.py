from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Sword', 50)

    def attack(self, dinosaur):
        pass