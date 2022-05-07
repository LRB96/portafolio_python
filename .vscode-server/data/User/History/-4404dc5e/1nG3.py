#Crear la función incializadora 



def run():
    numero = int(input("Escribe un número: "))

    if (numero ** 2) % 2 == 0:
        print("No es primo.")
    else:
        print("Es primo.")


if __name__ == "__main__":
    run()