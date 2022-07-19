import random

class Unit:
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intellect = intellect


    def __str__(self):
        return (f"i am {self.name}, my stats naw is health:[{self.health}], power:[{self.power}],"
                f" agility:[{self.agility}], intellect:[{self.intellect}]")

    def heal_me(self):
        hp = self.health
        if hp < 100:
            random_power_of_healing = random.randint(1, 20) / 100
            treatment = hp + (hp * random_power_of_healing)
            if treatment > 100:
                treatment = 100
                self.health = treatment
                return (f"Application of the drug, now my Heal Point is:{treatment}")
            else:
                self.health = treatment
                return (f"Application of the drug, now my Heal Point is:{treatment}")
        return ("i have maximum Heal Points, i can't heal")



    def loss_of_health(self):
        hp = self.health
        if hp > 0:
            random_damage = random.randint(1, 20) / 100
            damage = hp - (hp * random_damage)
            if damage < 0:
                damage = 0
                self.health = damage
                return (f"Oh, i got damage, now my Heal Point is: {damage}")
            else:
                self.health = damage
                return (f"Oh, i got damage, now my Heal Point is: {damage}")
        return ("i haven't Heal Points")

    def get_level_up(self):
        if self.power < 10:
            self.power += 1
            return




class Mage(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        magic_type = ["Water", "Fire", "Air"]
        self.type_of_magic = random.choice(magic_type)

    def __str__(self):
        return str(super().__str__()) + ", " + f"my class is Mage {self.type_of_magic}"

    def get_level_up(self):
        if self.intellect < 10:
            self.intellect += 1
            return super().__str__() + f" my class is Mage {self.type_of_magic}"
        else:
            return super().__str__() + f" my class is Mage {self.type_of_magic}, my level is max"

class Archer(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        bow_type = ["Bow", "Crossbow", "Sling"]
        self.type_of_bow = random.choice(bow_type)

    def __str__(self):
        return str(super().__str__()) + ", " + f"my class is Archer with {self.type_of_bow}"

    def get_level_up(self):
        if self.agility < 10:
            self.agility += 1
            return super().__str__() + f" my class is Archer with {self.type_of_bow}"
        else:
            return super().__str__() + f" my class is Archer with {self.type_of_bow}, my level is max"

class Knight(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        weapon_type = ["Sword", "Axe", "Pike"]
        self.type_of_weapon = random.choice(weapon_type)

    def __str__(self):
        return str(super().__str__()) + ", " + f"my class is Knight with {self.type_of_weapon}"

    def get_level_up(self):
        if self.power < 10:
            self.power += 1
            return super().__str__() + f" my class is Knight with {self.type_of_weapon}"
        else:
            return super().__str__() + f" my class is Knight with {self.type_of_weapon}, my level is max"

if __name__ == "__main__":
    U0 = Unit("Subaru")
    print(U0)
    print(U0.loss_of_health())
    print(U0.heal_me())

    gendalf = Mage("Gendalf")
    print(gendalf)
    print(gendalf.loss_of_health())
    print(gendalf.heal_me())
    print(gendalf.get_level_up())


    legolas = Archer("Legolas"  )
    print(legolas)
    print(legolas.loss_of_health())
    print(legolas.heal_me())
    print(legolas.get_level_up())

    sauron = Knight("Sauron")
    print(sauron)
    print(sauron.loss_of_health())
    print(sauron.heal_me())
    print(sauron.get_level_up())
