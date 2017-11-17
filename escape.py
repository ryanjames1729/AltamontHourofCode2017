#escape.py
import time

health = 2
knife = False
gun = False
combo = 1234
showerTime = 0

def door():
    print("The door is locked. Enter the combination to try to unlock it.")
    guess = int(input("> "))
    if guess == combo:
        print("You won the game, you're set free, not dead...")
    else:
        print("Hahahaha.")
        livingRoom()

def start():
    print("Welcome to the House of Horrors....")
    time.sleep(5)
    livingRoom()

def livingRoom():
    print()
    print("You are in the living room.")
    print("1) To enter the kitchen")
    print("2) To enter the bathroom")
    print("3) To open the door")
    print("4) To lay on the couch and cry")
    choice = int(input("> "))
    if choice == 1:
        kitchen()
    elif choice == 2:
        bathroom()
    elif choice == 3:
        door()
    elif choice == 4:
        time.sleep(30)
        livingRoom()
    else:
        print("Try another choice.")
        livingRoom()

def kitchen():
    global knife
    print()
    print("You are in the kitchen.")
    print("1) To enter the living room")
    print("2) To look in the fridge")
    print("3) To look in the drawers")
    choice = int(input("> "))
    if choice == 1:
        livingRoom()
    elif choice == 2:
        print("Nothing really in the fridge, so sorry.")
        kitchen()
    elif choice == 3 and knife == False:
        print("You found a knife.")
        knife = True
        kitchen()
    elif choice == 3 and knife == True:
        print("Nothing in the drawers.")
        kitchen()
    else:
        print("Try another choice.")
        kitchen()

def bathroom():
    global gun
    global showerTime
    print()
    print("You are in the bathroom.")
    print("1) To enter the living room")
    print("2) To look in the shower")
    print("3) To look in the cabinet")
    choice = int(input("> "))
    if choice == 1:
        livingRoom()
    elif choice == 2 and showerTime == 0:
        zombie()
        showerTime += 1
    elif choice == 2 and showerTime > 0:
        print("Nothing but a dead zombie")
        bathroom()
    elif choice == 3 and gun == False:
        print("You found a gun.")
        gun = True
        bathroom()
    elif choice == 3 and gun == True:
        print("Nothing in the cabinet.")
        bathroom()
    else:
        print("Try another choice.")
        bathroom()

def zombie():
    global health, knife, gun
    print()
    print("There is a zombie, what to do....?")
    weapons = []
    weapons.append("Fists")
    if knife:
        weapons.append("Knife")
    if gun:
        weapons.append("Gun")
    print("Your options are: " + str(weapons))
    choice = input("> ")
    if choice == "Fists" or choice == "fists":
        death()
    elif knife and (choice == "Knife" or choice == "knife"):
        print("The zombie is dead")
        health -= 1
        bathroom()
    elif gun and (choice == "Gun" or choice == "gun"):
        print("The zombie is dead")
        bathroom()
    else:
        zombie()

def death():
    print("Hah, you're dead.")

#Line below starts the game.
start()
