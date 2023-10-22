from decimal import Decimal
productsString = input("podaj produkty: ")
pricesString = input("podaj ceny: ")

products = productsString.split(',')
prices = pricesString.split(',')

productPricesMap = dict()

for product in products:
    productPricesMap[product] = Decimal(prices[products.index(product)])
print(productPricesMap)