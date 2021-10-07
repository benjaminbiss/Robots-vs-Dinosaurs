import random
from weapon import Weapon

class Robot:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapons = []
        self.power = 40
        self.power_drain = [0, 20, 30]

    def attack(self, dinosaur):
        weapon = self.choose_weapon()
        dinosaur.health = dinosaur.health - self.weapons[weapon - 1].attack_power
        self.power = self.power - self.power_drain[weapon - 1]

    def ai_attack(self, dinosaur):
        weapon = random.randint(0, 3)
        dinosaur.health = dinosaur.health - self.weapons[weapon - 1].attack_power
        self.power = self.power - self.power_drain[weapon - 1]
        print(f'{dinosaur.name} was hit for {self.weapons[weapon - 1]} damage!')

    def create_weapons(self):
        self.weapons.append(Sword)
        self.weapons.append(Rifle)
        self.weapons.append(Blaster)

    def choose_weapon(self):
        return int(input('Choose your weapon: 1. Sword   2. Rifle   3. Blaster'))


Sword = Weapon('Sword', 30)
Rifle = Weapon('Rifle', 50)
Blaster = Weapon('Blaster', 70)