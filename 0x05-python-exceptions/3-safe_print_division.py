#!/usr/bin/pyton3
def safe_print_division(a, b):
    try:
        result = a/b
    except(ZeroDivisionError, TypeError):
        result = none
    finally:
        print("Inside result: {}" .format(result))
        return result
