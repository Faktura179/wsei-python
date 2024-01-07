class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class ElectricalCar(Car):
    def __init__(self, make, model, range):
        Car.__init__(self, make, model)
        self.range = range

class SportsCar(Car):
    def __init__(self, make, model, max_speed):
        Car.__init__(self, make, model)
        self.max_speed = max_speed

class ElectricalSportsCar(ElectricalCar, SportsCar):
    def __init__(self, make, model, range, max_speed):
        ElectricalCar.__init__(self, make, model, range)
        SportsCar.__init__(self, make, model, max_speed)

    def print_info(self):
        print(f"Samochód elektryczny sportowy {self.make} {self.model} ma zasięg {self.range}km i osiąga maksymalną prędkość {self.max_speed}km/h.")

elektryczny_sportowy = ElectricalSportsCar("Tesla", "Model S", 400, 250)
elektryczny_sportowy.print_info()