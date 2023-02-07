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

    menu = int(input('Your choice: '))
    return menu

def continue_prompt(repeat):
    cont = input('Continue program? [y/n]: ')

    if cont == 'y' or cont == 'Y':
        repeat = True
    else:
        repeat = False
    return repeat

def select_menu(trx, menu):
    if menu == 1:
        print('\nAdd Item')
        item_name = input('Item Name: ')

        try:
            item_qty = int(input('Item Quantity: '))
        except ValueError:
            print('Input numbers only')
            item_qty = int(input('Item Quantity: '))

        try:
            item_price = int(input('Item Price: '))
        except ValueError:
            print('Input numbers only')
            item_price = int(input('Item Price: '))

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

        try:
            new_qty = int(input('New Item Quantity: '))
        except ValueError:
            print('Input numbers only')
            new_qty = int(input('New Item Quantity: '))

        trx.update_item_qty(item_name, new_qty)

    elif menu == 5:
        print('\nUpdate Item Price')
        item_name = input('Item Name: ')
        
        try:
            new_price = int(input('New Item Price: '))
        except ValueError:
            print('Input numbers only')
            new_price = int(input('New Item Price: '))
            
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