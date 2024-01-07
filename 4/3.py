class Employee:
    def __init__(self, name, age, position):
        self.__name = name
        self.__age = age
        self.__position = position

    def say_hello(self):
        print(f"{self.__name}, {self.__age} na pozycji {self.__position} mówi cześć!")
    
    def modify(self, name, age, position):
        self.__name = name
        self.__age = age
        self.__position = position

    def fire(self):
        print(f"{self.__name} został zwolniony!")
        self.__position = None


class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, enemy):
        print(f"{self.name} atakuje {enemy} i zadaje {self.damage} obrażeń!")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} został pokonany!")

    def display_info(self):
        print(f"Potwór {self.name}", end="")
        if self.health <= 0:
            print(" jest martwy.")
        else:
            print(f" ma {self.health} punktów życia i jego uderzenia zadają {self.damage} obrażeń.")


class Refrigerator:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if(len(self.items) >= self.capacity):
            print("Nie ma miejsca w lodówce na kolejne produkty!")
            return
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        print(f"Lodówa {self.brand} zawiera:")
        for item in self.items:
            print(f"\t{item}")

    def display_info(self):
        print(f"Marka: {self.brand}")
        print(f"Pojemność: {self.capacity} itemów")
        self.display_items()


employee = Employee("Janusz Palikot", 30, "Manager")
employee.say_hello()
employee.modify("Sławomir Nowak", 32, "Zegarmistrz")
employee.fire()

monster = Monster("Goblin", 10, 2)
monster.display_info()
monster.attack("Janusz")
monster.take_damage(9)
monster.display_info()
monster.take_damage(2)
monster.display_info()

fridge = Refrigerator("Samsung", 3)
fridge.add_item("Jajka")
fridge.add_item("Mleko")
fridge.add_item("Masło")
fridge.add_item("Ser")
fridge.display_items()
fridge.remove_item("Masło")
fridge.display_info()