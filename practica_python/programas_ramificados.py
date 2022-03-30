nombre_persona_1 = input("Nombre de la primera persona: ")
nombre_persona_2 = input("Nombre de la segunda persona: ")

edad_persona_1 = int(input("Edad de la primera persona: "))
edad_persona_2 = int(input("Edad de la segunda persona: "))


if (edad_persona_1 > edad_persona_2):
    print(f"{nombre_persona_1} es mayor que {nombre_persona_2}")
elif(edad_persona_1 < edad_persona_2):
    print(f"{nombre_persona_1} es menor que {nombre_persona_2}")
else:
    print(f"{nombre_persona_1} y {nombre_persona_2} tienen la misma edad.")