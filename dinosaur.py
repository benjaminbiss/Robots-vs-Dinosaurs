class Dinosaur:
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attacks = ('Smash', 'Slash', 'Bite')
        self.attack_power = [30, 50, 70]

    def attack(self, robot):
        attack_choice = int(input(f'Choose your attack: 1. Smash  2. Slash  3. Bite'))
        robot.health = robot.health - self.attack_power[attack_choice - 1]