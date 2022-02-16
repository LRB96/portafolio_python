# pesos = input("¿Cuántos pesos tienes? ")
# pesos =  float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares =  str(dolares)
# print("Tienes $" + dolares + " Doláres.")

dolares = input("¿Cuántos Dólares tienes? ")
dolares = float(dolares)
valor_peso = 0.00025
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " Pesos Colombianos.")