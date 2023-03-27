#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Prints the result of a function that divides a by b
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
