from robot import Robot

class Fleet:
    
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)

robot1 = Robot('robot-001')
robot2 = Robot('robot-002')
robot3 = Robot('robot-003')