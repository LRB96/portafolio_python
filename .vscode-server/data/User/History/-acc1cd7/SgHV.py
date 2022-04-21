def run():
    my_list = [1, "hello", 4.5, True]
    my_dist = {"firstname": "Luis", "lastname": "Rojas"}

    my_super_list = [
        {"firstname": "Luis", "lastname": "Rojas"},
        {"firstname": "Felipe", "lastname": "Andrade"},
        {"firstname": "Andres", "lastname": "Gomez"},
        {"firstname": "Otto", "lastname": "Bismark"}
    ]
    my_super_dict = {
        "firstname": "Luis", "lastname": "Rojas",
        "firstname": "Felipe", "lastname": "Andrade",
        "firstname": "Andres", "lastname": "Gomez",
        "firstname": "Otto", "lastname": "Bismark"
    }

    for key, value in my_super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()