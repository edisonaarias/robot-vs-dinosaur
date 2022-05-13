from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self, names):
    
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def __init__(self):
        pass
    def run_game(self):
        pass
    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side cna win!\n')
        
    def battle_phase(self):

        self.dinosaur.Dinosaur_attack_power(self.dinosaur)
        self.robot.weapon_attack_power(self.robot)

        if self.Dinosaur_attack_power is True:
            print("robot attacks")
        elif self.Dinosaur_attack_power is False:
            print("dinosaur attacks")

        else:
             self.robot, self.dinosaur = 'health_not_at_zero'()




    def display_winner(self):
        print( "The winner has been decided")