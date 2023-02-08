import pandas as pd
from cashregister import *
from operations import *

print('Welcome to XYZ Supermarket!')

trx = {}
cust_ID = input('Please input your member ID: ')
trx[cust_ID] = Transaction()

repeat = True

while repeat == True:
    menu = ask_prompt()

    while menu not in [i for i in range(0,9)]: # Anticipating input other than 0 - 8.
        menu = ask_prompt()

    select_menu(trx[cust_ID], menu)
    repeat = continue_prompt(repeat)

    if repeat == False:
        print('\nProgram ended, here is your order')
        trx[cust_ID].check_order()
        trx[cust_ID].total_price()
        print('Thank you for shopping at XYZ Supermarket!')
    else:
        pass