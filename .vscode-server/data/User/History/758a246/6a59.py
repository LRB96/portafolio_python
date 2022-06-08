def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str
        return string
    return string * n