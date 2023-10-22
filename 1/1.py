import datetime
name = input("Podaj imie: ")
age = int(input("Podaj wiek: "))

print(f"Cześć {name}!\nTwoje imie ma {len(name)} liter i zaczyna się od {name[0]}\nTeraz masz {age} lat, a za rok będzie to {age+1}. Rok urodzenia to {datetime.datetime.now().year - age}")