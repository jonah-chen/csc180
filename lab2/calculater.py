import numpy as np

current_value = 0
memory_value = None
previous_value = None


def display_current_value():
    print("Current value:", current_value)


def add(to_add):
    global current_value, previous_value
    previous_value = current_value
    current_value += to_add


def subtract(to_subtract):
    global current_value, previous_value
    previous_value = current_value
    current_value -= to_subtract


def mult(to_multiply):
    global current_value, previous_value
    previous_value = current_value
    current_value *= to_multiply


def divide(to_divide):
    global current_value, previous_value
    previous_value = current_value
    if to_divide != 0:
        current_value /= to_divide
    else:
        print('Error! You cannot divide by zero. Sorry.')


def memory(value):
    global memory_value
    memory_value = value


def recall():
    global current_value, previous_value
    if memory_value is None:
        print('Error! There is nothing stored in memory yet!')
    else:
        previous_value = current_value
        current_value = memory_value


def undo():
    global previous_value, current_value
    if previous_value is None:
        print('Error! There is nothing else to undo!')
    else:
        current_value, previous_value = previous_value, current_value


if __name__ == '__main__':
    # Welcome message    
    print('Welcome to the calculator program.')
    display_current_value

    # instructions for calculater to execute
