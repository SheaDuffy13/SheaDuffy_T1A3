import random
import time
import clearing

import classes as c

running_game = True
menu = True
play = False

def save():
    save_list = [
        user_name,
        str(user.coinpurse),
        ",".join(user.linen_bag)
    ]
    with open("save.txt", "w") as f:
        f.write("\n".join(save_list))

def draw():
    print('Xx------------------------------xX')

# Home Screen
print('')
print("         ><><><><><><><><><><><><")
print("         ><><> Master Thief <><><")
print("         ><><><><><><><><><><><><")
print()
home_input = input('Press Enter to continue or e to exit.. ')
if home_input == 'e':
    exit()
else:
    clearing.clear()

# Main Program
while running_game:
    while menu:
        clearing.clear()
        draw()
        print(" 1. NEW GAME")
        print(" 2. LOAD GAME")
        print(" 3. QUIT GAME")
        draw()
        print("")
        choice = input('Select number: ')

        if choice == "1":
            user_name = input('Enter your thief\'s name: ')
            user = c.Player(user_name)
            user.coinpurse.set(0)
            user.linen_bag.set([])
            menu = False
            play = True

        if choice == "2":
            try:
                with open("save.txt") as f:
                    file = f.readlines()
                    user_name = file[0].strip()
                    user = c.Player(user_name)
                    user.coinpurse.set(int(file[1].strip()))
                    user.linen_bag.set(file[2].split(','))
                clearing.clear()
                menu = False
                play = True
            except OSError:
                print("Save file not available..")
                input("Press enter to go back: ")

        if choice == "3":
            quit()

    while play:
        save()
        clearing.clear()
        print(f"Welcome back, {user.name}. You have {user.coinpurse} in your coinpurse and {user.linen_bag} in your bag")

        user_input = input('Press e for main menu or s to steal from chest: ')
        if user_input == "e":
            play = False
            menu = True
            save()
            print("\nAutosaving...")
            time.sleep(0.4)
        if user_input == "s":
            old_chest = c.Chest(["rusty dagger"], 30)
            print(old_chest.loose_coins, old_chest.loose_items)
            time.sleep(0.7)
            old_chest.loot(user)
            print(old_chest.loose_coins)
            time.sleep(0.7)


        old_chest = Chest(["rusty dagger"], 30)
        print(old_chest.loose_coins, old_chest.loose_items)
        print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")
        time.sleep(2)
        old_chest.loot(user)
        print(f"{user.name} has {user.coinpurse} coins and {user.linen_bag} in their bag")