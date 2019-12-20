from knight import Knight
from wizard import Wizard
from thief import Thief
from maps import Maps
from monsters import Monsters
from treasure import Treasure
from User import User

import pickle
import sys
import time
import os.path
from random import randint
from copy import deepcopy
from thiefAI import ThiefAI
from wizardAI import WixardAI
from knightAI import KnightAI


class Menu:

    def __init__(self):

        os.system("cls")
        print(""" 
         
         
                                                   ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄           ▄████████ ███    █▄  ███▄▄▄▄        
                                                   ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄        ███    ███ ███    ███ ███▀▀▀██▄      
                                                   ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███        ███    ███ ███    ███ ███   ███      
                                                   ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███       ▄███▄▄▄▄██▀ ███    ███ ███   ███      
                                                   ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███      ▀▀███▀▀▀▀▀   ███    ███ ███   ███      
                                                   ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███      ▀███████████ ███    ███ ███   ███      
                                                   ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███        ███    ███ ███    ███ ███   ███      
                                                   ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀         ███    ███ ████████▀   ▀█   █▀       
                                                                                                                      ███    ███                           
                    """)
        print("\n")
        print("                                                                                              1-New Game              ")
        print("                                                                                              2-Load Game             ")
        print("                                                                                              3-Remove saved Game     ")
        print("                                                                                              4-Exit                  ")
        print("\n")
        print("                                                                                     Copyright 2019 Originals      ")
        print("\n")
        print("                                                                                     Made by: Estefan Rengifo Marin")
        print("                                                                                              Ludvig Carlsen       ")
        print("                                                                                              Yassin Imlil         ")
        print("                                                                                              Said Wattar          ")
        print("                                                                                              Alexander Jontchev   ")
        print("\n")


        self.active_hero = ''
        self.AI = False
        self.active_AI = ''

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

    def link_str_monster(self, monsters):
        # matches strings to objects
        global Monsters
        big_spider = Monsters('Big spider', 7, 1, 2, 3, 0.2)
        orc = Monsters('Orc', 6, 3, 4, 4, 0.1)
        troll = Monsters('Troll', 2, 4, 7, 2, 0.05)
        skeleton = Monsters('Skeleton', 4, 2, 3, 3, 0.15)
        list_monsters = [big_spider, orc, troll, skeleton]

        active_monsters = []
        for monster in monsters:
            for spawnobj in list_monsters:
                if monster == spawnobj.name:
                    active_monsters.append(spawnobj)
        active_monsters.append(self.active_hero)

        return active_monsters

    def link_str_treasures(self, treasures):

        loosecoins = Treasure('Loose coins', 2, 0.4)
        moneypouch = Treasure('Money pouch', 6, 0.2)
        goldjewelry = Treasure('Golden jewelry', 10, 0.15)
        gemstone = Treasure('Gemstone', 14, 0.1)
        smallchest = Treasure('Small chest', 20, 0.05)
        list_treasure = [loosecoins, moneypouch, goldjewelry, gemstone, smallchest]

        active_treasure = []
        for treasure in treasures:
            for spawnobj in list_treasure:
                if treasure == spawnobj.name:
                    active_treasure.append(spawnobj)
        return active_treasure

    def died_function(self):
        os.system("cls")
        print("""
        
        
                ▓██   ██▓ ▒█████   █    ██     ▄▄▄       ██▀███  ▓█████     ███▄    █  ▒█████  ▄▄▄█████▓    █     █░ ▒█████   ██▀███  ▄▄▄█████▓ ██░ ██▓██   ██▓
                 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒████▄    ▓██ ▒ ██▒▓█   ▀     ██ ▀█   █ ▒██▒  ██▒▓  ██▒ ▓▒   ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██░ ██▒▒██  ██▒
                  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒███      ▓██  ▀█ ██▒▒██░  ██▒▒ ▓██░ ▒░   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▀▀██░ ▒██ ██░
                  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄    ▓██▒  ▐▌██▒▒██   ██░░ ▓██▓ ░    ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█ ░██  ░ ▐██▓░
                  ░ ██▒▓░░ ████▓▒░▒▒█████▓     ▓█   ▓██▒░██▓ ▒██▒░▒████▒   ▒██░   ▓██░░ ████▓▒░  ▒██▒ ░    ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█▒░██▓ ░ ██▒▓░
                   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░   ░ ▒░   ▒ ▒ ░ ▒░▒░▒░   ▒ ░░      ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░░▒░▒  ██▒▒▒ 
                 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░   ░ ░░   ░ ▒░  ░ ▒ ▒░     ░         ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░    ░     ▒ ░▒░ ░▓██ ░▒░ 
                 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░   ▒     ░░   ░    ░         ░   ░ ░ ░ ░ ░ ▒    ░           ░   ░  ░ ░ ░ ▒    ░░   ░   ░       ░  ░░ ░▒ ▒ ░░  
                 ░ ░         ░ ░     ░              ░  ░   ░        ░  ░            ░     ░ ░                  ░        ░ ░     ░               ░  ░  ░░ ░     
                 ░ ░                                                                                                                                   ░ ░     
        
        
        
        
        
        """)
        if self.AI:
            nr_rooms = 0
            for row in map_choice.current_map:
                for room in row:
                    if room == 'O':
                        nr_rooms += 1
            print(f'AI died:\nmonsters defeate: {self.active_AI.defeated_monsters}\nWallet: {self.user.wallet}\nrooms been in:{nr_rooms}')

        replay = input("\n                                                            Do you want play again or exit the game ?"
                       "\n                                                            1-Play again"
                       "\n                                                            2-save game"
                       "\n                                                            3-Exit"
                       "\n                                                            >").strip()

        if replay == "1":
            menu.pick_character()
            menu.pick_map()
        elif replay == "2":
            dict_wallet = {self.active_hero: self.user.wallet}

            with open(self.file_saved, "rb") as file:
                x = file.read()
                read_hero_list = pickle.loads(x)
                read_hero_list.append(dict_wallet)
                with open(self.file_saved, "wb") as save_file:
                    binary_save = pickle.dumps(read_hero_list)
                    save_file.write(binary_save)
                    sys.exit()
        else:
            print("See you next time!")
            sys.exit()

    def win_function(self):
        os.system("cls")
        print("""
                ██╗    ██╗███████╗    ██╗  ██╗ █████╗ ██╗   ██╗███████╗     █████╗     ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗     ██████╗  ██████╗ ██╗███████╗██╗
                ██║    ██║██╔════╝    ██║  ██║██╔══██╗██║   ██║██╔════╝    ██╔══██╗    ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗██║██╔════╝██║
                ██║ █╗ ██║█████╗      ███████║███████║██║   ██║█████╗      ███████║    ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██████╔╝██║   ██║██║███████╗██║
                ██║███╗██║██╔══╝      ██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝      ██╔══██║    ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║██║╚════██║╚═╝
                ╚███╔███╔╝███████╗    ██║  ██║██║  ██║ ╚████╔╝ ███████╗    ██║  ██║    ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ██████╔╝╚██████╔╝██║███████║██╗
                 ╚══╝╚══╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═╝  
         """)
        if self.AI:
            nr_rooms = 0
            for row in map_choice.current_map:
                for room in row:
                    if room == 'O':
                        nr_rooms += 1
            print(
                f'AI died:\nmonsters defeate: {self.active_AI.defeated_monsters}\nWallet: {self.user.wallet}\nrooms been in:{nr_rooms}')

        replay = input(
            "\n                                                            Do you want play again or exit the game ?"
            "\n                                                            1-Play again"
            "\n                                                            2-save game"
            "\n                                                            3-Exit"
            "\n                                                            >").strip()

        if replay == "1":
            menu.pick_character()
            menu.pick_map()
        elif replay == "2":
            dict_wallet = {self.active_hero: self.user.wallet}

            with open(self.file_saved, "rb") as file:
                x = file.read()
                read_hero_list = pickle.loads(x)
                read_hero_list.append(dict_wallet)
                with open(self.file_saved, "wb") as save_file:
                    binary_save = pickle.dumps(read_hero_list)
                    save_file.write(binary_save)
        else:
            print("See you next time!")
            sys.exit()
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

    def battle(self, character1, character2):
        thief_special_dice_roll = (randint(0, 100) / 100)
        sum_attack = self.gen_attack_sum(sorted_initiative)
        sum_agility = self.gen_agility_sum(sorted_initiative)

        if sum_attack[character1] > sum_agility[character2]:
            if self.active_hero == character2 and count_shield == 1 and character2.name == "Knight":
                print("Knights special blocked the attack\n")
                return character2.durability
            print(character1.name + f' attacks {character2.name} and deals 1 damage')
            if character1.name == "Thief" and thief_special_dice_roll <= 0.25:
                print("Critical!")
                character2.durability -= 2
            else:
                character2.durability -= 1

        else:
            print(character1.name + ' tried to attack but missed\n')
        return character2.durability

    def escape_fight(self):
        escape_chance = randint(1, 100)

        if self.active_hero.name == "Wizard":
            if (escape_chance / 100) <= 0.8:
                return True
            else:
                return False
        else:
            if (escape_chance / 100) <= (self.active_hero.agility * 10 / 100):
                return True
            else:
                return False

    def fight(self, monsters, treasures):
        active_monsters = self.link_str_monster(monsters)
        active_treasures = self.link_str_treasures(treasures)
        global sorted_initiative
        sorted_initiative = self.sequence(active_monsters)
        fight_loop = True

        global count_shield
        count_shield = 1

        while fight_loop:
            for character in sorted_initiative:
                try:
                    print(character[0].name + f's health:  {character[0].durability}')
                except:
                    pass
            print('\nThe turn order is: ')
            count = 1
            for character in sorted_initiative:
                try:
                    print(str(count) + ': ' + character[0].name)
                    count += 1
                except:
                    pass
            option_input = ''
            if self.AI:
                time.sleep(4)
                option_input = self.active_AI.fighting(active_monsters)
            else:
                option_input = input('\nPress "1" to start fight ... \nPress "2" to try to escape ...\n>')

            if option_input == '1':
                os.system('cls')

                print("Fight ...")

                character1 = sorted_initiative[0][0]
                character2 = sorted_initiative[1][0]
                try:
                    if character1.type == 'monster':
                        character2 = self.active_hero
                except:
                    pass
                if self.battle(character1, character2) > 0:
                    if character2.name == "Knight":
                        count_shield += 1

                    if self.battle(character2, character1) > 0:
                        if character1.name == "Knight":
                            count_shield += 1
                        pass
                    else:
                        print('\n' + character1.name + ' died\n')
                        if character1.type == 'monster':
                            map_choice.monster_map[map_choice.current_position[0]][
                                map_choice.current_position[1]].clear()
                            map_choice.treasure_map[map_choice.current_position[0]][
                                map_choice.current_position[1]].clear()

                        else:
                            self.died_function()
                            break
                        sorted_initiative.pop(0)
                        self.active_AI.defeated_monsters += 1
                        if len(sorted_initiative) == 1:
                            for treasure in active_treasures:
                                self.user.wallet += treasure.value
                            map_choice.show_map()
                            break
                else:
                    print('\n' + character2.name + ' died\n')
                    if character2.type == 'monster':
                        map_choice.monster_map[map_choice.current_position[0]][map_choice.current_position[1]].clear()
                        map_choice.treasure_map[map_choice.current_position[0]][map_choice.current_position[1]].clear()
                    else:
                        self.died_function()
                        break
                    sorted_initiative.pop(1)
                    self.active_AI.defeated_monsters += 1
                    if len(sorted_initiative) == 1:
                        for treasure in active_treasures:
                            self.user.wallet += treasure.value
                        map_choice.show_map()
                        break
            else:
                if self.escape_fight():
                    os.system("cls")
                    print("You escaped!")
                    map_choice.escape_room(previous_position)
                    map_choice.show_map()
                    fight_loop = False
                else:
                    os.system("cls")
                    print("You failed to escape, now you need to survive")
                    for character in sorted_initiative:
                        if character[0].type == "monster":
                            self.battle(character[0], self.active_hero)

    def new_room_options(self):
        monsters = map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]
        treasures = map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]]
        self.active_AI.current_pos = (self.current_pos[0], self.current_pos[1])

        print("\nTreasures in this room:")

        for t in treasures:
            print(t, end=" | ")
        print()

        print("--------------------------------------------")

        print("\nMonsters in this room:")

        for m in monsters:
            print(m, end=" | ")
        print()

        print("--------------------------------------------\n")

        #print(f'\nMonsters in this room:   {monsters} \nTreasures in this rooms: {treasures}')
        if len(monsters) > 0:
            self.fight(monsters, treasures)

        elif len(treasures) > 0:
            treasures = self.link_str_treasures(treasures)
            for treasure in treasures:
                self.user.wallet += treasure.value
            map_choice.treasure_map[self.current_pos[0]][self.current_pos[1]].clear()

    def start_game(self):
        self.current_pos = ()
        global previous_position
        map_choice.exit_room = (randint(0, len(map_choice.current_map)-1), randint(0, len(map_choice.current_map)-1))

        while True:
            print('\nWallet: ' + str(self.user.wallet))
            print('\nUse these commands to move:\nW = up\nS = down\nA = left\nD = right\nSave = save\nE = exit')
            previous_position = deepcopy(map_choice.current_position)
            cmd = ''

            # ai input
            if self.AI:
                cmd = self.active_AI.movement
            else:
                cmd = input('>').lower().strip()
            if cmd == 'w':
                self.current_pos = map_choice.move_up()
                if type(self.current_pos) == type(True):
                    self.win_function()
                    break
                self.active_AI.change_direction(self.current_pos)
            elif cmd == 's':
                self.current_pos = map_choice.move_down()
                if type(self.current_pos) == type(True):
                    self.win_function()
                    break
                self.active_AI.change_direction(self.current_pos)
            elif cmd == 'a':
                self.current_pos = map_choice.move_left()
                if type(self.current_pos) == type(True):
                    self.win_function()
                    break
                self.active_AI.change_direction(self.current_pos)
            elif cmd == 'd':
                self.current_pos = map_choice.move_right()
                if type(self.current_pos) == type(True):
                    self.win_function()
                    break
                self.active_AI.change_direction(self.current_pos)
            elif cmd == 'save':

                self.file_saved = (self.charater_name + ".txt")

                dict_wallet = {self.active_hero: self.user.wallet}

                with open(self.file_saved, "rb") as file:
                    x = file.read()
                    read_hero_list = pickle.loads(x)
                    read_hero_list.append(dict_wallet)
                    with open(self.file_saved, "wb") as save_file:
                        binary_save = pickle.dumps(read_hero_list)
                        save_file.write(binary_save)
                print("Your game has been saved!")
                time.sleep(2)

            elif cmd == 'e':
                print('\nYour score is: ' + str(self.user.wallet), " points.")
                print("See you later!")
                sys.exit()

            os.system('CLS')
            map_choice.show_map()
            # change to 'or' later
            if len(map_choice.monster_map[self.current_pos[0]][self.current_pos[1]]) != 0 or len(
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
            self.active_AI = KnightAI()
            print(self.message)

        elif self.user_char_choice == "2":
            self.message = "You are a Wizard!"
            wizard_hero.ability_discription()
            self.active_hero = wizard_hero
            self.active_AI = WixardAI()
            print(self.message)

        elif self.user_char_choice == "3":

            self.message = "You are a Thief!"
            thief_AI = ThiefAI()
            thief_hero.ability_discription()
            self.active_hero = thief_hero
            self.active_AI = ThiefAI()
            print(self.message)
        global user
        self.user = User(self.charater_name, self.active_hero, 0, 0)

    def pick_AI(self):
        cmd = input('\n1:Do you want to play yourself\n2:Should an AI do it?\n>')
        if cmd == '2':
            self.AI = True


    def pick_map(self):
        os.system("cls")
        global map_choice

        map_choice = Maps()

        print("\nChoose your map size!")
        print("\n1- Small map 4x4\n2- Medium map 5x5\n3- Large map 8x8\n")

        self.user_map_choice = input("\n>").strip()
        os.system("cls")

        if self.active_hero.name == 'Knight':
            self.active_AI = KnightAI()
        elif self.active_hero.name == 'Thief':
            self.active_AI = ThiefAI()
        elif self.active_hero.name == 'Wizard':
            self.active_AI = WixardAI()

        if self.user_map_choice == "1":
            map_choice.create_small_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()
            self.active_AI.mapsz = 4

        elif self.user_map_choice == "2":
            map_choice.create_medium_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()
            self.active_AI.mapsz = 5


        elif self.user_map_choice == "3":
            map_choice.create_large_map()
            map_choice.show_map()
            map_choice.randomize_monster()
            map_choice.randomize_treasure()
            self.active_AI.mapsz = 8

        pos = ''
        if self.AI:
            pos = self.active_AI.corner
            print('je')
        else:
            pos = input('\nChoose in which corner to begin :\n'
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
        # ai input
        map_choice.place_player(cmd)
        map_choice.show_map()
        menu.start_game()

    def user_name_creation(self):

        question = "Hello and welcome to 'Dungeon Run'.\nChoose a username for your character and let's get started!"

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
        if os.path.exists(self.file_saved):
            with open(self.file_saved, "rb") as file:
                b_file = file.read()
                self.hero_list = pickle.loads(b_file)
        else:
            with open(self.file_saved, "wb+") as new_file:

                empty_hero_list = []
                initial_save = pickle.dumps(empty_hero_list)
                new_file.write(initial_save)


        if self.user_char_choice == "1":
            with open(self.file_saved, "a+") as file:
                pass
                #file.write(self.message + "\n")

        elif self.user_char_choice == "2":
            with open(self.file_saved, "a+") as file:
                pass
                #file.write(self.message + "\n")

        elif self.user_char_choice == "3":
            with open(self.file_saved, "a+") as file:
                pass
                #file.write(self.message + "\n")


    def load_game(self):

        self.show_saved_game = input("\nDo you want to show all the saved game ? y/n\n>").strip().lower()
        if self.show_saved_game == "y":
            for file in os.listdir("."):
                if file.endswith(".txt"):
                    print(os.path.join(file).strip(".txt"))

        self.charater_name = input("\nPlease Enter your character username :\n>").strip().capitalize()
        self.load_username = (self.charater_name + ".txt")
        print("\n")

        if os.path.exists(self.load_username):

            count = 0

            with open (self.load_username, "rb") as file:
                binary_load = file.read()
                files = pickle.loads(binary_load)

                for element in files:
                    for self.k, self.v in element.items():

                        count += 1
                        print(count, self.k.name, self.v)

            my_input = input("\nPick a saved file\n>")
            for k, v in files[int(my_input) - 1].items():

                self.user = User(self.charater_name, k, v, 0)
                print(f'\nYou have picked {k.name,v}')


            self.active_hero = self.k
            menu.pick_AI()
            menu.pick_map()

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

        self.menu_choice = input("\n>").strip()

        if self.menu_choice == "1":
            os.system("cls")
            menu.user_name_creation()
            menu.pick_character()
            menu.save_character()
            menu.pick_AI()
            menu.pick_map()

        elif self.menu_choice == "2":
            os.system("cls")
            menu.load_game()

        elif self.menu_choice == "3":
            os.system("cls")
            menu.delete_file()

        elif self.menu_choice == "4":
            os.system("cls")
            print("\nSee you later!")
            sys.exit()

        else:
            print("Please follow the instruction you Dum Ass!")
            time.sleep(1.5)


while 1:

    # Instance of the class Menu
    menu = Menu()
    menu.new_user_game()