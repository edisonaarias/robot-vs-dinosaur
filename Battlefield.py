from dinosaur import Dinosaur
from robot import Robot


class battlefield:
    def __init__(self):    
        self.robot = Robot("DG3")
        self.dinosaur = Dinosaur("Carnotaurus", 400)

    def run_game(self):
        # intro
        # display welcome
        self.display_welcome()

        # main game 
        # battle phase
        self.battle_phase()

        # endgame
        self.display_winner()

        # Dinosaur = Dinosaur("Head Bash", 400, "robot was hit")
        # Robot = Robot("Bone saw", 500, "dinosaur was hit")
        # Dinosaur = Dinosaur("Bite", 400, "robot was hit")

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side cna win!\n')
        
    def battle_phase(self):

        self.dinosaur.attack(self.dinosaur)
        self.robot.weapon_attack_power(self.robot)

        if self.Dinosaur_attack_power is True:
            print("robot attacks")
        elif self.Dinosaur_attack_power is False:
            print("dinosaur attacks")

        else:
                self.robot, self.dinosaur = 'health_not_at_zero'
                print("health not at zero")


    def display_winner(self):
        print( "The winner has been decided")