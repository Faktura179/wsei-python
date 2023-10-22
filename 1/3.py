incomeType = input("Podaj typ dochodu(r - roczny, m - miesieczny): ")
income = int(input("Podaj swój dochód: "))

yearly = None
match (incomeType):
    case "m":
        yearly = income * 12
    case "r":
        yearly = income
    case _:
        print("Bład")
        exit()

if(yearly < 120000):
    print(f"Zapłacisz {yearly*0.12} podatku")
else:
    print(f"Zapłacisz {(yearly-120000)*0.32 + 120000*0.12} podatku")