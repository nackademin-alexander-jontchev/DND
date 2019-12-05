from Heroes import Heroes
import os.path


class Menu:

    def __init__(self):

        print('-----Welcome to "Dungeon Run"-----')

        print("1-New Game")
        print("2-Load Game")
        print("3-Exit")

        self.menu_choice = input("\n>").strip()

    def pick_character(self):

        print("\nChoose your character!")

        # Here you can put the class heroes

        print("\n")
        self.user_char_choice = input(">").strip()

        if self.user_char_choice == "1":

            self.message = "You are a Knight!"
            print(self.message)

        elif self.user_char_choice == "2":

            self.message = "You are a Wizard!"
            print(self.message)

        elif self.user_char_choice == "3":

            self.message = "You are a Thief!"
            print(self.message)

    def user_name_creation(self):

        self.charater_name = input("\nPlease, Enter your username character :\n>").strip()

        print(f'Your character name {self.charater_name} has been created!')

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

            with open(self.load_username,"r") as file:

                files = file.readline()

                print(files)

        else:

            print("This game doesn't exist.")

    def new_user_game(self):

        if self.menu_choice == "1":

            menu.pick_character()

            menu.user_name_creation()

            menu.save_character()

        elif self.menu_choice == "2":

            menu.load_game()

        elif self.menu_choice == "3":

            print("\nSee you later!")

# Instance of the class Menu
menu = Menu()
menu.new_user_game()








