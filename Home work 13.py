import random

class Unit:
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intellect = intellect


    def __str__(self):
        return f"i am {self.name}, my stats naw is health:[{self.health}], power:[{self.power}], " \
               f"agility:[{self.agility}], intellect:[{self.intellect}]"

    def heal_me(self):
        hp = self.health
        if hp < 100:
            random_power_of_healing = random.randint(1, 20) / 100
            treatment = hp + (hp * random_power_of_healing)
            if treatment > 100:
                treatment = 100
                self.health = treatment
            else:
                self.health = treatment

    def loss_of_health(self):
        hp = self.health
        if hp > 0:
            random_damage = random.randint(1, 20) / 100
            damage = hp - (hp * random_damage)
            self.health = damage
            if damage < 0:
                damage = 0
                self.health = damage

    def get_level_up(self):
        pass

class Mage(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        magic_type = ["Water", "Fire", "Air"]
        self.type_of_magic = random.choice(magic_type)

    def __str__(self):
        return f"{super().__str__()},my class is Mage {self.type_of_magic}"

    def get_level_up(self):
        if self.intellect < 10:
            self.intellect += 1

class Archer(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        bow_type = ["Bow", "Crossbow", "Sling"]
        self.type_of_bow = random.choice(bow_type)

    def __str__(self):
        return f"{super().__str__()},my class is Archer with {self.type_of_bow}"

    def get_level_up(self):
        if self.agility < 10:
            self.agility += 1

class Knight(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        weapon_type = ["Sword", "Axe", "Pike"]
        self.type_of_weapon = random.choice(weapon_type)

    def __str__(self):
        return f"{super().__str__()}, my class is Knight with {self.type_of_weapon}"

    def get_level_up(self):
        if self.power < 10:
            self.power += 1

if __name__ == "__main__":

    U0 = Unit("Subaru")
    print(U0)
    U0.loss_of_health()
    U0.heal_me()
    print(U0)

    gendalf = Mage("Gendalf")
    print(gendalf)
    gendalf.loss_of_health()
    gendalf.heal_me()
    gendalf.get_level_up()
    print(gendalf)

    legolas = Archer("Legolas")
    print(legolas)
    legolas.loss_of_health()
    legolas.heal_me()
    legolas.get_level_up()
    print(legolas)

    sauron = Knight("Sauron")
    print(sauron)
    sauron.loss_of_health()
    sauron.heal_me()
    sauron.get_level_up()
    print(sauron)

