from knight import Knight
from wizard import Wizard
from thief import Thief
from maps import Maps

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

    #def new_room_mech(self):
        #print(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]])
        
    def start_game(self):
        self.current_pos = ()

        while True:
            print('w, s, a, d')
            cmd = input('>').lower().strip()
            if cmd == 'w':
                self.current_pos = map_choice.move_up()
            elif cmd == 's':
                self.current_pos = map_choice.move_down()
            elif cmd == 'a':
                self.current_pos = map_choice.move_left()
            elif cmd == 'd':
                self.current_pos = map_choice.move_right()                
            os.system('CLS')
            map_choice.show_map()
            print(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]])
            print(map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]])

            #if len(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]) != 0:
            
                

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

        map_choice = Maps()

        print("\nPlease, choose your map size!")
        print("\n1- Small map 4x4\n2- Medium map 5x5\n3- Large map 8x8\n")

        self.user_map_choice = input("\n>").strip()

        os.system("cls")

        if self.user_map_choice == "1":
            map_choice.create_small_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()

        elif self.user_map_choice == "2":
            map_choice.create_medium_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()

        elif self.user_map_choice == "3":
            map_choice.create_large_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()
            

        pos = input('choose in which corner to begin :'
                    '\n1: upper right '
                    '\n2: lower right '
                    '\n3: upper left'
                    '\n4: lower left'
                    '\n>')
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

        self.charater_name = input("\nPlease, Enter your username character :\n>").strip().capitalize()

        print("Creating your character ...")

        #time.sleep(2)

        print(f'Your character name {self.charater_name} has been created!')

        #time.sleep(3)

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

        self.show_saved_game = input("\nDo you want to show all the saved game ? y/n\n>").strip().lower()

        if self.show_saved_game == "y":

            for file in os.listdir("."):
                if file.endswith(".txt"):
                    print(os.path.join(file).strip(".txt"))

        else:
            pass

        self.check_username = input("\nPlease Enter your character username :\n>").strip().capitalize()

        self.load_username = (self.check_username + ".txt")

        if os.path.exists(self.load_username):

            with open(self.load_username, "r") as file:

                files = file.readline()

                print("Loading Game ...")

                #time.sleep(2)

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
        #time.sleep(2)
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

        else:
            print("Please follow the instruction you Dum Ass!")


# Instance of the class Menu
menu = Menu()
menu.new_user_game()
