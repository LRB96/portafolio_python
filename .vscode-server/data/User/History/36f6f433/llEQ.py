#Función inicializadora
#Función principal 
#En la función principal creo 2 variables
#La primera variable "palabar", en la cual guardo la palabra que le pido al usuario con input.
#La segunda variable "es_palindromo", en la cual guardo lo que me returna la función palindromo, y a la cual le paso como 







def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else: 
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo.")
    else:
        print("No es palindromo.")
    

if __name__ ==  "__main__":
    run()