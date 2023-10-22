age = int(input("Podaj wiek: "))
money = int(input("Podaj ile masz kasy: "))

if(age<18):
    print(f"Jesteś niepełnoletni, brakuje ci {18-age} lat do pełnoletności", end='')
else:
    print("Jesteś pełnoletni", end='')

print(" i ", end='')

if(money < 20):
    print(f"nie masz wystarczającej ilości pieniędzy - brakuje ci {20-money} ziko")
else:
    print("masz wystarczającą ilość pieniędzy")
