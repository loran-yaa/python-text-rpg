import random
import time

from historia import HISTORIA


def _safe_input(prompt):
    try:
        return input(prompt).strip()
    except EOFError:
        print("\nNo input available. Exiting the game.")
        raise SystemExit(0)


def start_combat(player, enemy):
    print(f"\nBattle:  A BATTLE BEGINS: {player.name} VS {enemy.name}! Battle:\n")

    dialogue_shown = False

    while player.is_alive() and enemy.is_alive():
        print(f"HP: {player.name}: {player.health}/{player.max_health} HP | Potions: {player.potions}")
        print(f"Enemy: {enemy.name}: {enemy.health}/{enemy.max_health} HP")
        print("--------------------------------------------------")
        print("[1] Attack")
        print("[2] Use healing potion")

        choice = _safe_input("\nChoose your action > ")

        if choice == "1":
            damage = random.randint(15, 25)
            enemy.take_damage(damage)
            print(f"\nWeapon: {player.name} hit {enemy.name} for {damage} damage!")
        elif choice == "2":
            if player.potions > 0:
                player.potions -= 1
                heal_amount = 35
                player.health = min(player.max_health, player.health + heal_amount)
                print(f"\nPotion: You used a potion! You recovered {heal_amount} HP.")
            else:
                print("\nNo: You have no potions left! You lose your turn!")
        else:
            print("\nWarning: Invalid action! You lose your turn.")

        if enemy.health <= (enemy.max_health / 2) and enemy.is_alive() and not dialogue_shown:
            if "wolf" in enemy.name.lower():
                print(HISTORIA["wolf_growl"])
            else:
                print(HISTORIA["orc_threat"])

            dialogue_shown = True

        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy_damage = random.randint(10, 20)
            player.health -= enemy_damage
            print(f"Impact: {enemy.name} hit {player.name} for {enemy_damage} damage!\n")
            time.sleep(1)

    if player.is_alive():
        print(f"\nVictory: You defeated the {enemy.name}!")
        return True

    print(f"\nDefeat: You were defeated by the {enemy.name}...")
    return False


# Backward-compatible aliases for older code paths
iniciar_combat = start_combat
iniciar_combate = start_combat
