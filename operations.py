from cashregister import *

def ask_prompt():
    '''Function to ask which operation to take'''

    print('\nType 1 to add item to your shopping cart')
    print('Type 2 to delete item')
    print('Type 3 to update item name')
    print('Type 4 to update item quantity')
    print('Type 5 to update item price')
    print('Type 6 to check your order')
    print('Type 7 to display total price')
    print('Type 8 to reset your shopping cart')
    print('Type 0 to exit')
    
    while True:
        try:
            menu = int(input('Your choice: '))
            break
        
        except ValueError:
            print('Please  enter number from 0 to 8')
            continue

    return menu

def continue_prompt(repeat):
    '''Function to ask whether the user still want to continue the program'''
    
    # Looping to make sure users only input y or n
    while True:
        try:
            cont = input('Do you want to make some changes on your cart? [y/n]: ')
            
            if cont == 'y' or cont == 'Y': # if y, then repeat becomes True and exit the loop
                repeat = True
                break
            
            elif cont == 'n' or cont == 'N': # if n, then repeat becomes False and exit the loop
                repeat = False
                break

            else: # Anything other than y or n will raise a ValueError
                print("Please input 'y' or 'n'")
                raise ValueError
        
        except ValueError: # Back to the loop
            continue

    return repeat

def select_menu(trx, menu):
    '''
    Function to select menu displayed by ask_prompt()
    
    select_menu(trx, menu)

    Parameters:
    trx     = transaction, class Transaction()
    menu    = menu choice selected by user, int
    
    '''
    if menu == 1:
        print('\nAdd Item')
        item_name = input('Item Name: ')
        
        # Looping to make sure that the user only inputs int
        while True:
            try: # Prompt to input Item quantity
                item_qty = int(input('Item Quantity: '))
                break # If true, exit the loop
            
            except ValueError:
                print('Input numbers only')
                continue # If false, go back to the loop
        
        # Looping to make sure that the user only inputs int
        while True:
            try:
                item_price = int(input('Item Price: '))
                break
            
            except ValueError:
                print('Input numbers only')
                continue

        trx.add_item(item_name, item_qty, item_price)
    
    elif menu == 2:
        print('\nDelete Item')
        item_name = input('Item Name: ')
        trx.delete_item(item_name)

    elif menu == 3:
        print('\nUpdate Item Name')
        item_name = input('Item Name: ')
        new_item_name = input('New Item Name: ')
        trx.update_item_name(item_name, new_item_name)

    elif menu == 4:
        print('\nUpdate Item Quantity')
        item_name = input('Item Name: ')

        # Looping to make sure that the user only inputs int
        while True:
            try:
                new_qty = int(input('New Item Quantity: '))
                break
            
            except ValueError:
                print('Input numbers only')
                continue

        trx.update_item_qty(item_name, new_qty)

    elif menu == 5:
        print('\nUpdate Item Price')
        item_name = input('Item Name: ')
        
        # Looping to make sure that the user only inputs int
        while True:
            try:
                new_price = int(input('New Item Price: '))
                break
            
            except ValueError:
                print('Input numbers only')
                continue

        trx.update_item_price(item_name, new_price)

    elif menu == 6:
        print('\nCheck Order')
        trx.check_order()

    elif menu == 7:
        print('\nDisplay Total Price')
        trx.total_price()

    elif menu == 8:
        print('\nReset Shopping Cart')
        trx.reset_transaction()

    else:
        pass