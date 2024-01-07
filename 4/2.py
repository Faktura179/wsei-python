class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self._x = 0

    def say_name(self):
        print(f"Jestem 'Rzułf {self.name}' i zasuwam z prędkością {self.speed}km/h.")

    def move(self, distance):
        self._x += distance

    def get_position(self):
        return self._x


t = Turtle("Jan", 5)
t.say_name()  
t.move(10)
print(t.get_position())
