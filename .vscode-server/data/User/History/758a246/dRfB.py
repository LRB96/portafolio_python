def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo cadenas de texto."
        return string * n
    return repeater


def run():
    repeater("Platzi")
    print(make_repeater_of(5))

if __name__ == "__main__":
    run()