from weapon import Weapon

class Robot:
    def __init__( self, name):
        self.robot_name = 'DG3'
        self.robot_health = 1200
        self.active_weapon = 'bone saw'
        self.weapon_attack_power = Weapon()
    def attack(self, dinosaur):
        dinosaur.health -= Weapon.attack_power
