#Crear la función incializadora 
#Crear función principal (run) 
#Crear variable para almacenar número que le pido al usuario con input, y convierto en entero con int.
#



def run():
    numero = int(input("Escribe un número: "))

    if (numero ** 2) % 2 == 0:
        print("No es primo.")
    else:
        print("Es primo.")


if __name__ == "__main__":
    run()