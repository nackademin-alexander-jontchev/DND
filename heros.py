class knight:
    def __init__(self, initiativ, durability, attack, agility):
        self.initiativ = 5
        self.durability = 9
        self.attack = 6
        self.agility = 5
        
    def ability_discription(self):
        print("You have chosen the noble knight")
        print(f"Initiativ =  {self.initiativ}")
        print(f"Durability = {self.durability}")
        print(f"Attack = {self.attack}")
        print(f"Agility = {self.agility}")
        print(f("The knigts speciall ability is shieldblock:\n att the start of a battle, the knight has a 100% chans of blocking the first attack"))
