import random


class Character:
    def __init__(self, name, health, is_player=False):
        self.name = name
        self.health = health
        self.max_health = health
        self.is_player = is_player
        self.potions = 2

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return self.health

    def attack(self, enemy):
        damage = random.randint(18, 28) if self.is_player else random.randint(10, 18)
        enemy.take_damage(damage)
        print(f"Battle: {self.name} attacked {enemy.name} for {damage} damage!")
        return damage

    def heal(self):
        if self.potions <= 0:
            print("No potions left!")
            return 0

        heal_amount = random.randint(25, 35)
        self.health = min(self.max_health, self.health + heal_amount)
        self.potions -= 1
        print(f"Potion: {self.name} used a potion and recovered {heal_amount} HP!")
        return heal_amount

    @property
    def vida(self):
        return self.health

    @vida.setter
    def vida(self, value):
        self.health = value

    @property
    def vida_maxima(self):
        return self.max_health

    @vida_maxima.setter
    def vida_maxima(self, value):
        self.max_health = value

    @property
    def pocoes(self):
        return self.potions

    @pocoes.setter
    def pocoes(self, value):
        self.potions = value

    @property
    def nome(self):
        return self.name

    @nome.setter
    def nome(self, value):
        self.name = value

    @property
    def esta_vivo(self):
        return self.is_alive()


# Backward-compatible alias for older project code
characters = Character
