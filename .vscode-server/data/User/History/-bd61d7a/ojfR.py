def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre: str) -> bool:
    return f"{nombre}, recibiste un mensaje"


print(mensaje(10))