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
        counter_robot = 0
        counter_dino = 0
        run = True
        while run == True:
            self.dino_turn()
            self.robo_turn()
            for robot in self.fleet.robots:
                if robot.health == 0:
                    counter_robot = counter_robot + 1
            for dino in self.herd.dinosaurs:
                if dino.health == 0:
                    counter_dino = counter_dino + 1
            if counter_dino == 3:
                self.display_winner('robots')
                run = False
            elif counter_robot == 3:
                self.display_winner('dinosaurs')
                run = False
            else:
                counter_robot = 0
                counter_dino = 0

    def dino_turn(self):
        if self.herd.dinosaurs[0].health > 0:
            index = self.show_robo_opponent_options()
            self.herd.dinosaurs[0].attack(self.fleet.robots[index - 1])
        elif self.herd.dinosaurs[1].health > 0:
            index = self.show_robo_opponent_options()
            self.herd.dinosaurs[1].attack(self.fleet.robots[index - 1])
        elif self.herd.dinosaurs[2].health > 0:
            index = self.show_robo_opponent_options()
            self.herd.dinosaurs[2].attack(self.fleet.robots[index - 1])
            

    def robo_turn(self):
        if self.fleet.robots[0].health > 0:
            index = self.show_dino_opponent_options()
            self.fleet.robots[0].attack(self.herd.dinosaurs[index - 1])
        elif self.fleet.robots[1].health > 0:
            index = self.show_dino_opponent_options()
            self.fleet.robots[1].attack(self.herd.dinosaurs[index - 1])
        elif self.fleet.robots[2].health > 0:
            index = self.show_dino_opponent_options()
            self.fleet.robots[2].attack(self.herd.dinosaurs[index - 1])          

    def show_dino_opponent_options(self):
        print(f'{self.herd.dinosaurs[0].name}: {self.herd.dinosaurs[0].health}hp, {self.herd.dinosaurs[1].name}: {self.herd.dinosaurs[1].health}hp, {self.herd.dinosaurs[2].name}: {self.herd.dinosaurs[2].health}hp')
        return int(input(f'Enter 1 for {self.herd.dinosaurs[0].name}, Enter 2 for {self.herd.dinosaurs[1].name}, Enter 3 for {self.herd.dinosaurs[2].name}'))
    
    def show_robo_opponent_options(self):
        print(f'{self.fleet.robots[0].name}: {self.fleet.robots[0].health}hp, {self.fleet.robots[1].name}: {self.fleet.robots[1].health}hp, {self.fleet.robots[2].name}: {self.fleet.robots[2].health}hp')
        return int(input(f'Enter 1 for {self.fleet.robots[0].name}, Enter 2 for {self.fleet.robots[1].name}, Enter 3 for {self.fleet.robots[2].name}'))

    def display_winner(self, string):
        if string == 'robots':
            print('The robots beat the dinosaurs!')
        elif string == 'dinosaurs':
            print('The dinosaurs beat the robots!')


robot_fleet = fleet.Fleet()
dino_herd = herd.Herd()