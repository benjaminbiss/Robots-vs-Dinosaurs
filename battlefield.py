from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle(self):
        self.dino_turn(self, self.herd.dinosaurs)
        self.robo_turn(self, self.fleet.robots)

    def dino_turn(self, dinosaurs):
        for dino in dinosaurs:
            if dino.health > 0:
                robot = self.show_robo_opponent_options()
                self.herd.dinosaurs[dino].attack(robot)
            else:
                 self.display_winner('robots')

    def robo_turn(self, robots):
        for robo in robots:
            if robo.health > 0:
                dinosaur = self.show_dino_opponent_options()
                self.fleet.robots[robo].attack(dinosaur)            
            else:
                 self.display_winner('dinosaurs')

    def show_dino_opponent_options(self):
        return
    
    def show_robo_opponent_options(self):
        return

    def display_winner(self, string):
        if string == 'robots':
            print('The robots beat the dinosaurs!')
        elif string == 'dinosaurs':
            print('The dinosaurs beat the robots!')