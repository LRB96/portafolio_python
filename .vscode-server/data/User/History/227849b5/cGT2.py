def prime_number(number: int) -> bool:
    if number%2 == 0:
        print("No es primo.")
    else:
        print("Es primo.")


def run():
    print(prime_number(3))

if __name__ == "__main__":
    run()