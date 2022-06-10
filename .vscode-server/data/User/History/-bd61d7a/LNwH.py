# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre: str):
#     return f"{nombre}, recibiste un mensaje"


# print(mensaje("César"))


def bohemian(func):
    def rapsody(text):
        return func(text) * 5
    return rapsody


@bohemian
def queen(string: str):
    return f"{string}"

print(queen("Galileo" + " "))


