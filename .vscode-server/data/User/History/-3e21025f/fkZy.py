def run():
    
    #list_comprehension
    my_list = range(0,101)
    new_list = [x**2 for x in my_list x%2 == 0]
    print(new_list)
    

    # for x in my_list:
    #     print(x**2)



if __name__ == "__main__":
    run()