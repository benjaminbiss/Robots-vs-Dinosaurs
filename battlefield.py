from fleet import Fleet
from herd import Herd

class Battlefield:
    
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        self.herd.create_herd(self)
        self.fleet.create_fleet(self)
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle(self):
        fighting = True
        while fighting == True:
            fighting = self.dino_turn()
            fighting = self.robo_turn()

    def dino_turn(self):
        for dino in self.herd.dinosaurs:
            if dino.health > 0:
                robot = self.show_robo_opponent_options()
                self.herd.dinosaurs[dino].attack(robot)
                return True
            else:
                 self.display_winner('robots')
                 return False

    def robo_turn(self):
        for robo in self.fleet.robots:
            if robo.health > 0:
                dinosaur = self.show_dino_opponent_options()
                self.fleet.robots[robo].attack(dinosaur)
                return True            
            else:
                 self.display_winner('dinosaurs')
                 return False

    def show_dino_opponent_options(self):
        for dinos in self.herd.dinosaurs:
            print(f'{self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp, {self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp, {self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp')
        dinasaur = input(f'Enter 1 for {self.herd.dinosaurs[0]}, Enter 2 for {self.herd.dinosaurs[1]}, Enter 3 for {self.herd.dinosaurs[2]}')
        return dinasaur
    
    def show_robo_opponent_options(self):
        for robo in self.fleet.robots:
            print(f'{self.fleet.robots.name}: {self.fleet.robots.health}hp, {self.fleet.robots.name}: {self.fleet.robots.health}hp, {self.fleet.robots.name}: {self.fleet.robots.health}hp')
        robot = input(f'Enter 1 for {self.fleet.robots[0]}, Enter 2 for {self.fleet.robots[1]}, Enter 3 for {self.fleet.robots[2]}')
        return robot

    def display_winner(self, string):
        if string == 'robots':
            print('The robots beat the dinosaurs!')
        elif string == 'dinosaurs':
            print('The dinosaurs beat the robots!')


robot_fleet = Fleet()
dino_herd = Herd()