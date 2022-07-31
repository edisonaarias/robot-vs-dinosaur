class Dinosaur:
    def __init__(self, name, attack_power,) -> None:
        self.name = name
        self.attack_power = attack_power 
        self.health =  100 

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"Hit! {robot.name} now has {robot.health}")