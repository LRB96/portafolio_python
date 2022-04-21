def run():
    
    #list_comprehension
    new_list = [x**2 for x in range(0,101) if x%3 != 0]
    print(new_list)
    

    # for x in my_list:
    #     print(x**2)



if __name__ == "__main__":
    run()