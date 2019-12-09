
class knight:

    def __init__(self):
        self.initiative = 5
        self.durability = 9
        self.attack = 6
        self.agility = 5
        
    def ability_discription(self):
        print("\n1-Knight\n")

        print(f"Initiative =  {self.initiative}")
        print(f"Durability = {self.durability}")
        print(f"Attack = {self.attack}")
        print(f"Agility = {self.agility}")
        print(f"The knight speciall ability is shieldblock:\nAt the start of a battle, the knight has a 100% chans of blocking the first attack")



