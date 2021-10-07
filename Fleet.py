from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        self.robots[0].create_weapons()
        self.robots[1].create_weapons()
        self.robots[2].create_weapons()

    def choose_robot(self):
        return int(input(f'Choose your robot: {self.robots[0].name}: {self.robots[0].health}hp, {self.robots[0].power}mp,  {self.robots[1].name}: {self.robots[1].health}hp, {self.robots[1].power}mp,  {self.robots[2].name}: {self.robots[2].health}hp, {self.robots[2].power}mp'))

robot1 = Robot('robot-001')
robot2 = Robot('robot-002')
robot3 = Robot('robot-003')