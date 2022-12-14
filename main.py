import random
import time
import clearing
from simple_term_menu import TerminalMenu
import ast

#pages
import classes as c
import art

RUNNING_GAME = True
MENU = True
PLAY = False
INVENTORY_MENU_RUN = False
CABIN = False
WELL = False

def save():
    save_list = [
        user_name,
        str(user.coinpurse),
        ''.join(str(user.linen_bag)),
        str(user.fishbucket)
    ]
    with open("save.txt", "w") as sf:
        sf.write("\n".join(save_list))

# Home Screen
clearing.clear()
c.home_screen_img()
input("\n    Press Enter to continue... \n")
# clearing.clear()

# Main Program
while RUNNING_GAME:
    while MENU:
        clearing.clear()
        art.draw()
        print(" 1. NEW GAME")
        print(" 2. LOAD GAME")
        print(" 3. QUIT GAME")
        art.draw()
        print("")
        choice = input('Select number: ')

        #New Game
        if choice == "1":
            clearing.clear()
            user_name = input('Enter your name: ')
            user = c.Player(user_name)
            user.coinpurse.set(0)
            user.linen_bag.set([])
            user.fishbucket.set(0)
            clearing.clear()
            print(f"\nWelcome, {user_name}. To make selections enter the prompted letter or number.\n")
            print("To continue, hit Enter. This game auto saves.")
            input("\n\n\ncontinue..")
            MENU = False
            PLAY = True

        #Load Game
        elif choice == "2":
            try:
                with open("save.txt") as sf:
                    file = sf.readlines()
                    user_name = file[0].strip()
                    usr_inv_load = ast.literal_eval(str(file[2].strip()))
                    user = c.Player(user_name)
                    user.coinpurse.set(int(file[1]))
                    user.linen_bag.set(usr_inv_load)
                    user.fishbucket.set(int(file[3]))
                clearing.clear()
                MENU = False
                PLAY = True
            except OSError:
                clearing.clear()
                print("Save file not available..")
                input("\ncontinue..")

        #Exit Game
        elif choice == "3":
            clearing.clear()
            print(art.road_art)
            print("Aight Imma head out..\n")
            time.sleep(0.7)
            quit()
        else:
            print("\nType the number of your preferred option then press Enter..")
            time.sleep(2)
            clearing.clear()

    # INVENTORY MENU
    while INVENTORY_MENU_RUN:
        usr_inv = ast.literal_eval(str(user.linen_bag))
        inventory_menu_items = ["back", "", f"{user.fishbucket} fish"] + usr_inv
        inventory_menu = TerminalMenu(
            inventory_menu_items,
            title = f"{user_name}'s Inventory\n",
            skip_empty_entries = True,
            clear_screen = True
        )
        inv_sel = inventory_menu.show()
        if inv_sel == 0:
            INVENTORY_MENU_RUN = False
            PLAY = True
        if inv_sel == 2:
            print(art.bucket_art)
            if user.fishbucket.coins is 0:
                print("empty..")
                input("\n\ncontinue..")
            else:
                print("\nthe stench of fish is overwhelming..")
                input("\n\ncontinue..")
        if inv_sel >= 3:
            print(f"\n{user_name}'s newly aquired {inventory_menu_items[inv_sel]}.. \nMaybe this will fetch some coins")
            if inventory_menu_items[inv_sel] == "worn book":
                print("\nYou turn the book over to read the title.. 'The Lusty Argonian Maid'")
            input("\n\ncontinue..")

    # MAIN GAME
    while PLAY:
        save()
        clearing.clear()
        print(art.mountain_art)
        print(f"You stand at a crossroads in the mountains. Upon checking your coinpurse you have {user.coinpurse} coins.")
        print("You see a lake in one direction and a cabin in another.")
        print("\nc: go to cabin  \nf: fish at the lake          m: main menu \ni: inventory                 e: exit game")
        user_input = input("\n:")
        if user_input == "m":
            PLAY = False
            MENU = True
            save()
            time.sleep(0.4)

        if user_input == "c":
            while True:
                clearing.clear()
                print(art.cabin_art)
                print("You've approached a lone cabin. It looks like no one is home. You also see an old well behind the cabin.")
                print(" a: approach cabin \n w: investigate well \n e: go back")
                c_input = input("\n :")
                if c_input == "a":
                    CABIN = True
                    while CABIN:
                        clearing.clear()
                        print(art.room_art)
                        print("You slipped into the cabin and see 3 old chests in the corner.\n")
                        print("1: open 1st chest \n2: open 2nd chest \n3: open 3rd chest \ne: leave\n")
                        c_input = input(":")
                        if c_input == "1":
                            c.old_chest1.loot(user)
                            continue
                        elif c_input == "2":
                            c.old_chest2.loot(user)
                            continue
                        elif c_input == "3":
                            c.old_chest3.loot(user)
                            continue
                        elif c_input == "e":
                            CABIN = False
                        else:
                            continue
                elif c_input == "w":
                    WELL = True
                    while WELL:
                        clearing.clear()
                        print(art.well_art)
                        print("You approach the old well and see a crank to pull up the bucket. \nb: investigate bucket \ne: leave")
                        w_input = input(":")
                        if w_input == "b":
                            c.well_chest.loot(user)
                        elif w_input == "e":
                            WELL = False
                        else:
                            continue

                elif c_input == "e":
                    CABIN = False
                    clearing.clear()
                    print(art.road_art)
                    print("time to head back..")
                    time.sleep(1.4)
                    break
                else:
                    continue
        #Run Fishing
        elif user_input == "f":
            import fishing as f
            f.fishing()
            clearing.clear()
            print(art.road_art)
            print(f"You came back from the trip with {f.fish} fish..")
            user.fishbucket.add(f.fish)
            print(f"{user.fishbucket} total in inventory..")
            input("\n\ncontinue..")

        #Open Inventory
        elif user_input == "i":
            PLAY = False
            INVENTORY_MENU_RUN = True
        elif user_input == "e":
            clearing.clear()
            print(art.road_art)
            print("Aight Imma head out..\n")
            time.sleep(0.7)
            PLAY = False
            RUNNING_GAME = False
        else: continue
