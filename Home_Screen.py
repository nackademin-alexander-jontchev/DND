from knight import Knight
from wizard import Wizard
from thief import Thief
from maps import Maps

import time
import os.path
import sys
from random import randint


class Menu:

    def __init__(self):
        # Visuals to make the starting menu looks good.
        os.system("cls")
        print("##################################")
        print('#    Welcome to "Dungeon Run     #')
        print("##################################")
        print("\n")
        print("          1-New Game              ")
        print("          2-Load Game             ")
        print("          3-Remove saved Game     ")
        print("          4-Exit                  ")
        print("\n")
        print("     Copyright 2019 Originals     ")

        self.menu_choice = input("\n>").strip()

        os.system("cls")

    #def new_room_mech(self):
        #print(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]])

    # Function to create the user profile.
    def user_name_creation(self):

        question = "Hello champion, What's your username, if you don't have one, just pick one and let's get started ?"

        for char in question :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        self.charater_name = input("\n>").strip().capitalize()

        question2 = "Creating your character ...\n"

        for char in question2 :
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)

        question3 = f'Your character name {self.charater_name} has been created!'

        for char in question3:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(2)

        os.system("cls")

    # Function to pick the hero
    def pick_character(self):

        question = f'Hello {self.charater_name}, what hero do you want to play ?'

        for char in question:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
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

    # Function to pick the map size.
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

        pos = input('\nChoose in which corner you want to begin :'
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

    # Function to start the new game in the menu.
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

    # Function to start the game.
    def start_game(self):

        self.current_pos = ()

        while True:

            print('Use these command to move:\nW = up\nS = down\nA = left\nD = right')
            cmd = input('>').lower().strip()

            if cmd == 'w':
                self.current_pos = map_choice.move_up()

            elif cmd == 's':
                self.current_pos = map_choice.move_down()

            elif cmd == 'a':
                self.current_pos = map_choice.move_left()

            elif cmd == 'd':
                self.current_pos = map_choice.move_right()

            os.system('cls')
            map_choice.show_map()

            print(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]])
            print(map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]])

            # if len(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]) != 0:

    # Function to save the hero
    def save_character(self):

        self.file_saved = (self.charater_name + ".txt")

        if self.user_char_choice == "1":
            with open(self.file_saved, "a+") as file:
                file.write(self.message + "\n")

        elif self.user_char_choice == "2":
            with open(self.file_saved, "a+") as file:
                file.write(self.message + "\n")

        elif self.user_char_choice == "3":
            with open(self.file_saved, "a+") as file:
                file.write(self.message + "\n")

    # Function to load the hero
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

                files = file.read()

                print("Loading Game ...")

                time.sleep(2)

                print(files)


        else:

            print("This game doesn't exist.")

    # Function to delete the profile
    def delete_file(self):
        try:


            for file in os.listdir("."):
                if file.endswith(".txt"):
                    print(os.path.join(file).strip(".txt"))

            self.remove_file = input("\nWhich saved game you want to remove ?\n").strip()

            self.remove_file = (self.remove_file + ".txt")

            os.remove(self.remove_file)
            print("Removing saved game ...")
            time.sleep(2)
            print("Game removed!")

        except:

            print("File not found. ")


# Instance of the class Menu
menu = Menu()
menu.new_user_game()
