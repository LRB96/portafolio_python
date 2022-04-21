def run():
    my_list = [range(0,101)]

    new_list = [x for x in my_list x^2]
    print(new_list)



if "__name__" == "__main__":
    run()