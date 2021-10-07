from dinosaur import Dinosaur

class Herd:
    
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)

    def choose_dino(self):
        return int(input(f'Choose your dinosaur: {self.dinosaurs[0].name}: {self.dinosaurs[0].health}, {self.dinosaurs[1].name}: {self.dinosaurs[1].health}, {self.dinosaurs[2].name}: {self.dinosaurs[2].health}'))



dino1 = Dinosaur('Terry')
dino2 = Dinosaur('Larry')
dino3 = Dinosaur('Marry')