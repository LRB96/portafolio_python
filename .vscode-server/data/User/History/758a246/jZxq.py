def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo cadenas de texto."
        return string * n
    return repeater


def run():
    make_repeater_of(5)
    print(repeater("Platzi"))

if __name__ == "__main__":
    run()