#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    old_list = []
    for i in range(0, list_length):
        try:
            numb = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            numb= 0
        except ZeroDivisionError:
            print("division by zero")
            numb= 0
        except IndexError:
            print("out of range")
            numb= 0
        finally:
            old_list.append(numb)
    return(old_list)
