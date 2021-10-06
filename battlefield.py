import fleet
import herd

class Battlefield:
    
    def __init__(self):
        self.fleet = fleet.Fleet()
        self.herd = herd.Herd()

    def run_game(self):
        self.herd.create_herd()
        self.fleet.create_fleet()
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
            if self.herd.dinosaurs[0].health > 0:
                robot = self.show_robo_opponent_options()
                self.herd.dinosaurs[0].attack(robot)
                return True
            elif self.herd.dinosaurs[1].health > 0:
                robot = self.show_robo_opponent_options()
                self.herd.dinosaurs[1].attack(robot)
                return True
            elif self.herd.dinosaurs[2].health > 0:
                robot = self.show_robo_opponent_options()
                self.herd.dinosaurs[2].attack(robot)
                return True
            else:
                 self.display_winner('robots')
                 return False

    def robo_turn(self):
        for robo in self.fleet.robots:
            if self.fleet.robots[0].health > 0:
                dinosaur = self.show_dino_opponent_options()
                self.fleet.robots[0].attack(dinosaur)
                return True 
            elif self.fleet.robots[1].health > 0:
                dinosaur = self.show_dino_opponent_options()
                self.fleet.robots[1].attack(dinosaur)
                return True 
            elif self.fleet.robots[2].health > 0:
                dinosaur = self.show_dino_opponent_options()
                self.fleet.robots[2].attack(dinosaur)
                return True            
            else:
                 self.display_winner('dinosaurs')
                 return False

    def show_dino_opponent_options(self):
        for dinos in self.herd.dinosaurs:
            print(f'{self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp, {self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp, {self.herd.dinosaurs.name}: {self.herd.dinosaurs.health}hp')
        dinasaur = input(f'Enter 1 for {self.herd.dinosaurs[0]}, Enter 2 for {self.herd.dinosaurs[1]}, Enter 3 for {self.herd.dinosaurs[2]}')
    
    def show_robo_opponent_options(self):
            print(f'{self.fleet.robots[0].name}: {self.fleet.robots[0].health}hp, {self.fleet.robots[1].name}: {self.fleet.robots[1].health}hp, {self.fleet.robots[2].name}: {self.fleet.robots[2].health}hp')
        robot = input(f'Enter 1 for {self.fleet.robots[0]}, Enter 2 for {self.fleet.robots[1]}, Enter 3 for {self.fleet.robots[2]}')

    def display_winner(self, string):
        if string == 'robots':
            print('The robots beat the dinosaurs!')
        elif string == 'dinosaurs':
            print('The dinosaurs beat the robots!')


robot_fleet = fleet.Fleet()
dino_herd = herd.Herd()