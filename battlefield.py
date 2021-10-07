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
            for dino in self.herd.dinosaurs:
                if dino.health <= 0:
                    counter_dino = counter_dino + 1            
            if counter_dino == 3:
                self.display_winner('robots')
                run = False
                break
            self.dino_turn()
            for robot in self.fleet.robots:
                if robot.health <= 0:
                    counter_robot = counter_robot + 1            
            if counter_robot == 3:
                self.display_winner('dinosaurs')
                run = False
                break
            self.robo_turn()
            counter_robot = 0
            counter_dino = 0

    def dino_turn(self):
        dino_choice = self.herd.choose_dino()
        while self.herd.dinosaurs[dino_choice - 1].health <= 0:
            print('Choose a dinosaur with health! That one is dead!')
            dino_choice = self.herd.choose_dino()
        index = self.show_robo_opponent_options()
        self.herd.dinosaurs[dino_choice - 1].attack(self.fleet.robots[index - 1])
            
    def robo_turn(self):
        robot_choice = self.fleet.choose_robot()
        while self.fleet.robots[robot_choice - 1].health <= 0:
            print('Choose a robot with health! That one is dead!')
            robot_choice = self.fleet.choose_robot()
        index = self.show_dino_opponent_options()
        self.fleet.robots[robot_choice - 1].attack(self.herd.dinosaurs[index - 1])    

    def show_dino_opponent_options(self):
        return int(input(f'Choose who you want to attack: 1.{self.herd.dinosaurs[0].name}: {self.herd.dinosaurs[0].health}hp, 2.{self.herd.dinosaurs[1].name}: {self.herd.dinosaurs[1].health}hp, 3.{self.herd.dinosaurs[2].name}: {self.herd.dinosaurs[2].health}hp'))
    
    def show_robo_opponent_options(self):
        return int(input(f'Choose who you want to attack: 1.{self.fleet.robots[0].name}: {self.fleet.robots[0].health}hp, 2.{self.fleet.robots[1].name}: {self.fleet.robots[1].health}hp, 3.{self.fleet.robots[2].name}: {self.fleet.robots[2].health}hp'))

    def display_winner(self, string):
        if string == 'robots':
            print('The robots beat the dinosaurs!')
        elif string == 'dinosaurs':
            print('The dinosaurs beat the robots!')


robot_fleet = fleet.Fleet()
dino_herd = herd.Herd()