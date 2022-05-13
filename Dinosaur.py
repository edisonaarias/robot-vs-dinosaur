class Dinosaur:
    def __init__(self, name, attack_power):
        self.Dinosaur_name = name
        self.Dinosaur_attack_power = attack_power 
        self.Dinosaur_health =  1400 

    def attack(self, robot):
        robot.health -= self.Dinosaur_attack_power