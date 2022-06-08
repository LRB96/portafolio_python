def mayusculas(func):
    def envoltura(texto):
        return func(texto).uppe()


