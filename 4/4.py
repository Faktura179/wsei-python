import random;
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} lata.")

class Sparrow(Bird):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def fly(self):
        print(f"{self.name} lata powoli.")

class Eagle(Bird):
    def __init__(self, name, beak_length):
        super().__init__(name)
        self.beak_length = beak_length

    def fly(self):
        print(f"{self.name} szybuje.")

class Warrior:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, warrior):
        damage = warrior.get_hit(self)
        print(f"{self.name} atakuje zadając {damage} obrażeń.")
        if(warrior.health <= 0):
            print(f"{warrior.name} został pokonany!")

    def get_hit(self, warrior):
        self.health -= warrior.strength
        return warrior.strength

class Player(Warrior):
    def __init__(self, name, health, strength, level, companion):
        super().__init__(name, health, strength)
        self.level = level
        self.armour = 1
        self.companion = companion

    def level_up(self):
        self.level += 1
        print(f"Gracz {self.name} wylewelował do {self.level} poziomu.")
        self.companion.fly()
        random_number = random.randint(1, 3)
        if random_number == 1:
            self.health += 1
            print(f"{self.name} otrzymał 1pkt zdrowia.")
        elif random_number == 2:
            self.strength += 1
            print(f"{self.name} otrzymał 1pkt siły.")
        else:
            self.armour += 1
            print(f"{self.name} otrzymał 1pkt odporności.")

    def get_hit(self, warrior):
        damage = warrior.strength - self.armour
        if damage < 0:
            damage = 0
        self.health -= damage
        return damage
       

sparrow = Sparrow("Jacek Wróbel", 12)
sparrow.fly()

eagle = Eagle("Orzeł 1", 5)
eagle.fly()

monster = Warrior("Elf", 4, 4)
player = Player("Lara Croft", 10, 2, 1, eagle)

player.attack(monster)
monster.attack(player)
player.attack(monster)
player.level_up()