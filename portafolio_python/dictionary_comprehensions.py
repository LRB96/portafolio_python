def run():
    # for i in range(1,101):
    #     cube_root = i ** 3
    #     if i % 3 != 0:
    #         print(str(i) + " elevado al cubo es: " + str(cube_root))

    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)

if __name__ == "__main__":
    run()


        # cube_nums = {
        #     "Number: " + str(i), "  ", " Cube_Root: " + str(i)
        #     }
        # cube_nums = "".join(cube_nums)

# def run():

#     my_dict = {i : round(i**3,2) for i in  range(1,101)}

#     print(my_dict)

# if __name__=='__main__':
#     run()