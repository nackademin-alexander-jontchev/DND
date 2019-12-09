class wizard:

    def __init__(self):
        self.initiative = 6
        self.durability = 4
        self.attack = 9
        self.agility = 5

    def ability_discription(self):
        print("\n2-Wizard\n")

        print(f"Initiative =  {self.initiative}")
        print(f"Durability = {self.durability}")
        print(f"Attack = {self.attack}")
        print(f"Agility = {self.agility}")
        print(f"The Wizards speciall ability is Illumination:\nThe wizard can blind the monsters and has an 80% chance to escape fights")
