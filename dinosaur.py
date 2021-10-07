import random


class Dinosaur:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attacks = ('Smash', 'Slash', 'Bite')
        self.attack_power = [30, 50, 70]
        self.energy = 40
        self.energy_drain = [0, 20, 30]

    def attack(self, robot):
        attack_choice = int(input(f'Choose your attack: 1. Smash  2. Slash  3. Bite'))
        robot.health = robot.health - self.attack_power[attack_choice - 1]
        self.energy = self.energy - self.energy_drain[attack_choice - 1]

    def ai_attack(self, robot):
        attack_choice = random.randint(0, 3)
        robot.health = robot.health - self.attack_power[attack_choice - 1]
        self.energy = self.energy - self.energy_drain[attack_choice - 1]
        print(f'{robot.name} was hit for {self.attack_power[attack_choice - 1]} damage!')