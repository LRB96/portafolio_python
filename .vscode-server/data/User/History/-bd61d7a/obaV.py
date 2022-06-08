def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
