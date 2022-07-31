from battlefield import battlefield
from dinosaur import Dinosaur
from robot import Robot

dino_test = Dinosaur("Carnotaurus", 25)
robo_test = Robot("DG3 Test")

dino_test.attack(robo_test)
robo_test.attack(dino_test)

battle = battlefield()
battle.run_game()