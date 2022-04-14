def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"fistname": "luis", "lastname": "rojas"}
    
    super_list = [
        {"firstname": "luis", "lastname": "rojas"},
        {"firstname": "andres", "lastname": "gomez"},
        {"firstname": "manuel", "lastname": "diaz"},
        {"firstname": "francesca", "lastname": "buovino"}
    ]
    
    # print(super_list)
    
    for i in super_list:
        print(i.items())
    
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.5,3.6,4.8]
    }
    
    for key, value in super_dict.items():
        print(key, "", value)



if __name__ == "__main__":
    run()