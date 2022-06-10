# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre: str):
#     return f"{nombre}, recibiste un mensaje"


# print(mensaje("César"))


def bohemian(func):
    def rapsody(Galileo):
        for i in range(5):
            print("Galileo")
        # return func(Galileo) * 5
    return rapsody


@bohemian
def queen(Figaro: str):
    return f"{Figaro}, Magnificooooo!"

queen()