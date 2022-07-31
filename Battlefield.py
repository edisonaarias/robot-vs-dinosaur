from dinosaur import Dinosaur
from robot import Robot
import random


class battlefield:
    def __init__(self):    
        self.robot = Robot("DG3")
        self.dinosaur = Dinosaur("Carnotaurus", 25)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle_phase(self):
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            random_roll = random.randint(1,10)
            if random_roll % 2 == 0:
                self.robot.attack(self.dinosaur)
            else:
                self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.robot.health <= 0:
            print("Dinosaur won!")
        else:
            print("Robot won!")
