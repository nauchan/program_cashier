import pandas as pd
from cashregister import *
from operations import *

print('Welcome to XYZ Supermarket!')

trx = Transaction()
repeat = True

while repeat == True:
    try:
        menu = ask_prompt()
        while menu not in [i for i in range(0,9)]: # Anticipating input other than 0 - 8.
            menu = ask_prompt()

    except ValueError: # In case the input is not int, input again.
        print('Wrong input, please enter number from 0 to 8')
        menu = ask_prompt()

    select_menu(trx, menu)
    repeat = continue_prompt(repeat)

    if repeat == False:
        print('\nProgram ended, here is your order')
        trx.check_order()
        trx.total_price()
    else:
        pass