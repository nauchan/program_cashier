import pandas as pd
from cashregister import *
from operations import *

print('Welcome to XYZ Supermarket!')

# Customers can input their own membership ID
# Membership IDs are saved in trx
trx = {}
cust_ID = input('Please input your member ID: ')
trx[cust_ID] = Transaction()

repeat = True # Used for looping in case the user does not want to end the program

# Looping in case the user does not want to end the program
while repeat == True:
    menu = ask_prompt() # Ask which menu to take

    while menu not in [i for i in range(0,9)]: # Anticipating input other than 0 - 8
        menu = ask_prompt()

    select_menu(trx[cust_ID], menu) # Selecting menu or operations

    repeat = continue_prompt(repeat) # Ask to continue or end the program, if end, then repeat = False

    if repeat == False: # Quit loop
        print('\nProgram ended, here is your order')
        trx[cust_ID].check_order()
        trx[cust_ID].total_price()
        print('Thank you for shopping at XYZ Supermarket!')
        
    else:
        pass