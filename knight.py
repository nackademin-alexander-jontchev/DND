class Knight:

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
        print(f"The knight special ability is shieldblock:\nAt the start of a battle, the knight has a 100% chance of blocking the first attack")


        print("\n1-Knight")
        print(f" ---------------")
        print(f"| Initiative = {self.initiative}|")
        print(f"| Durability = {self.durability}|")
        print(f"| Attack     = {self.attack}|")
        print(f"| Agility    = {self.agility}|")
        print(f" ---------------")
        print(f"\n Special ability :----------------------------------------------------")
        print(f"|The knight always blocks the first attack per battle with his shield,|\n"
              f"|and therefore need not avoid or take any damage                      |")
        print(f" ---------------------------------------------------------------------")

