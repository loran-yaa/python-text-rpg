import random
import time

from characters import Character
from combat import start_combat
from historia import HISTORIA


# A simple helper to avoid repeating the input loop

def ask_choice(message, valid_choices):
    while True:
        try:
            choice = input(message).strip()
        except EOFError:
            print("\nNo input available. The game will close.")
            raise SystemExit(0)

        if choice in valid_choices:
            return choice

        print(f"Note: Invalid option! Please type only: {', '.join(valid_choices)}.")


# --- CITY MODULE ---
def enter_tavern(player):
    input("\n[ENTER] to enter the Golden Boar Tavern...")
    print(HISTORIA["tavern"])

    challenge = ask_choice("What is your plan? [1 or 2] > ", ["1", "2"])

    if challenge == "1":
        print("\nStrength: You grab the mercenary's hand. The table creaks!")
        time.sleep(1)
        if random.choice([True, False]):
            print("Victory: You win! You slam his arm against the table!")
            print('Beer: Mercenary: "Nice, kid! You have strength!"')
            return True

        print("Impact: You were crushed against the table...")
        print('Laugh: Mercenary: "You need gym time, kid!"')
        return False

    print('\nMind: Mercenary: "Alright, smart one! Answer this:"')
    print("   'What creature has the body of a lion, wings of an eagle and solves riddles?'")
    print("   [1] Chimera | [2] Sphinx | [3] Manticore")

    answer = ask_choice("\nChoose > ", ["1", "2", "3"])
    if answer == "2":
        print('\nMind: Mercenary: "Now that is what I call intelligence!"')
        return True

    print('\nMind: Mercenary: "Wrong! It was the Sphinx! Go study!"')
    return False


def visit_forge(player):
    input("\n[ENTER] to go to the Steel Forge...")
    print("\n--- STEEL FORGE ---")
    print('Smith: Grom the Blacksmith: "You can choose ONE item on me!"')
    print(f"Status: {player.health}/{player.max_health} HP | Potions: {player.potions}\n")
    print("[1] Iron Shield (+20 Max HP)")
    print("[2] Potion Belt (+2 Potions)")

    item = ask_choice("\nChoose your item [1 or 2] > ", ["1", "2"])
    if item == "1":
        player.max_health += 20
        player.health += 20
        print(f"Shield: You now have {player.max_health} maximum HP!")
        return

    player.potions += 2
    print(f"Potion: You now have {player.potions} potions in your belt!")


def city_arc(player):
    print(HISTORIA["art_city"])
    print(HISTORIA["city_intro"])

    name = input('Old Historian: "What is your name, young one?"\n> ').strip()
    if name:
        player.name = name

    print(f'\nOld man: Historian: "Take care in Aethelgard, {player.name}!"')

    if enter_tavern(player):
        print(HISTORIA["mercenary_lore"])
    else:
        print('\nBeer: Mercenary: "You lost, but here is the hint: visit the blacksmith before you die in the streets."\n')

    visit_forge(player)

    input("\n[ENTER] to climb to the Sanctuary...")
    print(HISTORIA["shrine_p1"])
    input("\n[ENTER] to continue...")
    print(HISTORIA["shrine_p2"])
    input("\n[ENTER] to receive the blessing...")
    print(HISTORIA["shrine_p3"])

    player.health = player.max_health
    print("\nHP FULLY RESTORED BY AERITH'S POWERS!")
    print(f"HP: {player.health}/{player.max_health}\n")
    input("[ENTER] to march into the Dark Forest...")


# --- FOREST MODULE ---
def forest_arc(player):
    print(HISTORIA["art_forest"])
    print(HISTORIA["forest_mental"])

    input("\n[ENTER] to advance through the darkness...")
    print(HISTORIA["lake_wolf"])

    wolf_action = ask_choice("How will you approach the wolf? [1 or 2] > ", ["1", "2"])

    if wolf_action == "1":
        print(HISTORIA["wolf_attack"])
        input("\n[ENTER] to draw your sword...")
        wolf = Character("Sacred Wolf", health=110, is_player=False)
        return start_combat(player, wolf)

    print(HISTORIA["wolf_tamed"])
    return True


# --- MAIN FUNCTION ---
def play_game():
    print(HISTORIA["intro"])
    path = ask_choice("Path [1 or 2] > ", ["1", "2"])

    player = Character("Hero", health=100, is_player=True)
    orc = Character("Guardian Orc", health=80, is_player=False)

    if path == "1":
        print(HISTORIA["path_1"])
        player.max_health += 20
        player.health += 20
    else:
        print(HISTORIA["path_2"])
        player.health -= 15

    input("\n[ENTER] to fight the Orc!")

    if not start_combat(player, orc):
        print(HISTORIA["defeat"])
        return

    print(HISTORIA["victory_after_battle"])
    destination = ask_choice("Destination [1 or 2] > ", ["1", "2"])

    if destination == "2":
        city_arc(player)

    if not forest_arc(player):
        print(HISTORIA["defeat"])
        return

    print("\nYou survived this stage of the adventure!")
    input("\n[ENTER] to close the game...")


if __name__ == "__main__":
    play_game()
