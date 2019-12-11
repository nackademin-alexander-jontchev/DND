from knight import Knight
from wizard import Wizard
from thief import Thief
from maps import Maps
from monsters import Monsters
from treasure import Treasure

import sys
import time
import os.path
from random import randint


class Menu:

    def __init__(self):

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

        self.active_hero = ''
        self.menu_choice = input("\n>").strip()
        os.system("cls")

    def sort_fight_order(self, fight_order_list):
        n = len(fight_order_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if fight_order_list[j][1] < fight_order_list[j + 1][1]:
                    fight_order_list[j], fight_order_list[j + 1] = fight_order_list[j + 1], fight_order_list[j]
        return fight_order_list

    def sequence(self, list_of_participants):
        # sorts by initiative
        fight_order = []
        for participant in list_of_participants:
            fighter_list = []
            sum_of_ini = 0
            for dice in range(participant.initiative):
                dice_number = randint(1, 6)
                sum_of_ini += dice_number
            fighter_list.append(participant)
            fighter_list.append(sum_of_ini)
            fight_order.append(fighter_list)

            fight_order = self.sort_fight_order(fight_order)

        return fight_order

    def link_str_obj(self, monsters, treasure):
        # matches strings to objects
        global Monsters
        big_spider = Monsters('big spider', 7, 1, 2, 3, 0.2)
        orc = Monsters('orc', 6, 3, 4, 4, 0.1)
        troll = Monsters('troll', 2, 4, 7, 2, 0.05)
        skeleton = Monsters('skeleton', 4, 2, 3, 3, 0.15)
        loosecoins = Treasure('loose coins', 2, 0.4)
        moneypouch = Treasure('money pouch', 6, 0.2)
        goldjewelry = Treasure('golden jewelry', 10, 0.15)
        gemstone = Treasure('gemstone', 14, 0.1)
        smallchest = Treasure('small chest', 20, 0.05)
        list_monsters = [big_spider, orc, troll, skeleton]
        active_monsters = []
        for monster in monsters:
            for spawnobj in list_monsters:
                if monster == spawnobj.name:
                    active_monsters.append(spawnobj)
        active_monsters.append(self.active_hero)
        return active_monsters

    def gen_attack_sum(self, sorted_initiative):
        dict_attack_sum = {}
        for character in sorted_initiative:
            sum_attack = 0
            for x in range(character[0].attack):
                dice = randint(1, 6)
                sum_attack += dice
            dict_attack_sum[character[0]] = sum_attack
        return dict_attack_sum

    def gen_agility_sum(self, sorted_initiative):
        dict_agility_sum = {}
        for character in sorted_initiative:
            sum_agility = 0
            for x in range(character[0].attack):
                dice = randint(1, 6)
                sum_agility += dice
            dict_agility_sum[character[0]] = sum_agility
        return dict_agility_sum

    def fight(self, monsters, treasures):
        active_monsters = self.link_str_obj(monsters, treasures)
        sorted_initiative = self.sequence(active_monsters)
        sum_attack = self.gen_attack_sum(sorted_initiative)
        print(sum_attack)
        sum_agility = self.gen_agility_sum(sorted_initiative)
        print(sum_agility)

    def new_room_options(self):
        monsters = map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]
        treasures = map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]]
        print(f'\nMonsters in this room:   {monsters} \nTreasures in this rooms: {treasures}')
        cmd = input('\nDo you wish to fight? y/n\n>').lower().strip()
        if cmd == 'y':
            self.fight(monsters, treasures)

    def start_game(self):
        self.current_pos = ()
        while True:
            print('Use these command to move:\nW = up\nS = down\nA = left\nD = right\nE = exit')
            cmd = input('>').lower().strip()
            if cmd == 'w':
                self.current_pos = map_choice.move_up()
            elif cmd == 's':
                self.current_pos = map_choice.move_down()
            elif cmd == 'a':
                self.current_pos = map_choice.move_left()
            elif cmd == 'd':
                self.current_pos = map_choice.move_right()
            elif cmd == 'e':
                print("See you later!")
                sys.exit()

            os.system('CLS')
            map_choice.show_map()
            if len(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]) != 0 and len(
                    map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]]) != 0:
                self.new_room_options()

    def pick_character(self):

        question = f'Hello {self.charater_name}. Select the hero you want to play ?'

        for char in question:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        # Here you can put the class heroes

        knight_hero = Knight()
        knight_hero.ability_discription()
        time.sleep(0.05)
        wizard_hero = Wizard()
        wizard_hero.ability_discription()
        time.sleep(0.05)
        thief_hero = Thief()
        thief_hero.ability_discription()

        print("\n")
        self.user_char_choice = input(">").strip()

        os.system("cls")

        if self.user_char_choice == "1":

            self.message = "You are a Knight!"
            knight_hero.ability_discription()
            self.active_hero = knight_hero
            print(self.message)

        elif self.user_char_choice == "2":

            self.message = "You are a Wizard!"
            wizard_hero.ability_discription()
            self.active_hero = wizard_hero
            print(self.message)

        elif self.user_char_choice == "3":

            self.message = "You are a Thief!"
            thief_hero.ability_discription()
            self.active_hero = thief_hero
            print(self.message)

    def pick_map(self):
        global map_choice

        map_choice = Maps()

        print("\nChoose your map size!")
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
        
        os.system("cls")

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

        question = "Hello and welcome to 'Dungeon Run'.\nchoose a username for your character and let's get started!"

        for char in question:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        self.charater_name = input("\n>").strip().capitalize()

        question2 = "\nCreating your character ...\n"

        for char in question2:
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