from knight import Knight
from wizard import Wizard
from thief import Thief
from maps import maps

import time
import os.path
from random import randint


class Menu:

    def __init__(self):

        print('-----Welcome to "Dungeon Run"-----')

        print("1-New Game")
        print("2-Load Game")
        print("3-Remove saved Game")
        print("4-Exit")

        self.menu_choice = input("\n>").strip()

        os.system("cls")


    def gen_treasure(self):
        spawned = []
        treasures = {'lösa slantar':40, 'pengapung': 20, 'guldsmycken': 15, 'ädelsten': 10, 'liten skattkista': 5}
        for k,v in treasures.items():
            chance = randint(0,100)
            if chance <= v:
                spawned.append(k)
        return spawned
                
    def gen_monster(self):
        pass
    def fight_monster(self):
        pass
    

    def start_game(self):

        while True:
            print('w, s, a, d')
            cmd = input('')
            if cmd == 'w':
                map_choice.move_up()
                menu.gen_monster()
                menu.fight_monster()
                menu.gen_treasure()

            elif cmd == 's':
                map_choice.move_down()
                menu.gen_monster()
                menu.fight_monster()
                menu.gen_treasure()
            elif cmd == 'a':
                map_choice.move_left()
                menu.gen_monster()
                menu.fight_monster()
                menu.gen_treasure()
            elif cmd == 'd':
                map_choice.move_right()
                menu.gen_monster()
                menu.fight_monster()
                menu.gen_treasure()
            os.system('CLS')
            map_choice.show_map()
    
    
    
    def pick_character(self):

        print("\nChoose your character!")

        # Here you can put the class heroes

        knight_hero = Knight()
        knight_hero.ability_discription()

        wizard_hero = Wizard()
        wizard_hero.ability_discription()

        thief_hero = Thief()
        thief_hero.ability_discription()


        print("\n")
        self.user_char_choice = input(">").strip()

        os.system("cls")

        if self.user_char_choice == "1":

            self.message = "You are a Knight!"
            knight_hero.ability_discription()
            print(self.message)

        elif self.user_char_choice == "2":

            self.message = "You are a Wizard!"
            wizard_hero.ability_discription()
            print(self.message)

        elif self.user_char_choice == "3":

            self.message = "You are a Thief!"
            thief_hero.ability_discription()
            print(self.message)


    def pick_map(self):
        global map_choice

        map_choice = maps()

        print("\nPlease, choose your map size!")
        print("\n1- Small map 4x4\n2- Medium map 5x5\n3- Large map 8x8\n")

        self.user_map_choice = input("\n>").strip()

        os.system("cls")

        if self.user_map_choice == "1":
            map_choice.create_small_map()
            map_choice.show_map()

        elif self.user_map_choice == "2":
            map_choice.create_medium_map()
            map_choice.show_map()

        elif self.user_map_choice == "3":
            map_choice.create_large_map()
            map_choice.show_map()


        pos = input('choose in which corner to begin \n 1: upper right \n 2: lower right \n 3: upper left \n 4: lower left\n>')
        cmd = ''
        if pos == '1':
            cmd = 'ur'
        elif pos == '2':
            cmd = 'lr'
        elif pos == '3':
            cmd = 'ul'
        elif pos == '4':
            cmd = 'll'

        map_choice.place_player(cmd)
        map_choice.show_map()
        menu.start_game()

    def user_name_creation(self):

        self.charater_name = input("\nPlease, Enter your username character :\n>").strip()

        print("Creating your character ...")

        time.sleep(2)

        print(f'Your character name {self.charater_name} has been created!')

        time.sleep(3)

        os.system("cls")

    def save_character(self):

        self.file_saved = (self.charater_name + ".txt")

        if self.user_char_choice == "1":
            with open(self.file_saved,"a+") as file:
                file.write(self.message)

        elif self.user_char_choice == "2":
            with open(self.file_saved, "a+") as file:
                file.write(self.message)

        elif self.user_char_choice == "3":
            with open(self.file_saved, "a+") as file:
                file.write(self.message)

    def load_game(self):

        self.show_saved_game = input("\nDo you want to show all the saved game ? y/n\n>").strip()

        if self.show_saved_game == "y":

            for file in os.listdir("."):
                if file.endswith(".txt"):
                    print(os.path.join(file).strip(".txt"))

        else:
            pass

        self.check_username = input("\nPlease Enter your character username :\n>").strip()

        self.load_username = (self.check_username + ".txt")

        if os.path.exists(self.load_username):

            with open(self.load_username, "r") as file:

                files = file.readline()

                print("Loading Game ...")

                time.sleep(2)

                print(files)

        else:

            print("This game doesn't exist.")

    def delete_file(self):

        for file in os.listdir("."):
            if file.endswith(".txt"):
                print(os.path.join(file).strip(".txt"))

        self.remove_file = input("\nWhich saved game you want to remove ?\n").strip()

        self.remove_file = (self.remove_file + ".txt")

        os.remove(self.remove_file)
        print("Removing saved game ...")
        time.sleep(2)
        print("Game removed!")


    def new_user_game(self):

        if self.menu_choice == "1":

            menu.user_name_creation()

            menu.pick_character()

            menu.save_character()

            menu.pick_map()

        elif self.menu_choice == "2":

            menu.load_game()

        elif self.menu_choice == "3":

            menu.delete_file()

        elif self.menu_choice == "4":

            print("\nSee you later!")


# Instance of the class Menu
menu = Menu()
menu.new_user_game()
