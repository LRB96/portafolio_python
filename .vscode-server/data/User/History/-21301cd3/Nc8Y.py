def run():
    my_list = range(1,6)
    squares = [i**2 for i in my_list]
    print(squares)
    
    squares2 = list(map(lambda x: x**2, my_list))



if __name__ == "__main__":
    run()