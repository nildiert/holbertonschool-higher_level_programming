#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            division = my_list_1[x] / my_list_2[x]
            new_list.append(division)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except (TypeError, ValueError):
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
    return new_list
