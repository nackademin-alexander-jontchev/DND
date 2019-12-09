class thief():

    def __init__(self):
        self.initiative = 7
        self.durability = 5
        self.attack = 5
        self.agility = 7

    def ability_discription(self):
        print("\n3-Thief\n")

        print(f"Initiative =  {self.initiative}")
        print(f"Durability = {self.durability}")
        print(f"Attack = {self.attack}")
        print(f"Agility = {self.agility}")
        print(f"The Critical strike\nThe thief has a 25% to do double damage everytime the thief attacks")
