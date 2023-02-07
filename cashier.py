import pandas as pd

class Transaction:
    def __init__(self):
        '''Initialize shopping cart dictionary'''
        self.cart = dict()
    
    def add_item(self, item_name, item_qty, item_price):
        '''
        Method to add item to the shopping cart. If the item already exists
        in the cart, it will add the item quantity and ignore the item price.
        
        add_item(item_name, item_qty, item_price)
        
        Parameters:
        item_name  = name of item, str
        item_qty   = quantity of item, int
        item_price = price of item, int
        '''
        try: # Add item_qty if the item already existed in cart
            self.cart[item_name][0] = self.cart[item_name][0] + item_qty
            self.cart[item_name][2] = self.cart[item_name][0] * self.cart[item_name][1]
            
        except KeyError: # Add item to cart
            self.cart.update({item_name : [item_qty, item_price, item_qty*item_price]})
    
    def update_item_name(self, item_name, new_item_name):
        '''
        Method to update item name in the shopping cart.
        
        update_item_name(item_name, new_item_name)
        
        Parameters:
        item_name     = name of item to be replaced, str
        new_item_name = new item name, str
        '''
        try: # Update item name if the item exists in cart
            temp = self.cart[item_name]
            self.cart.pop(item_name)
            self.cart.update({new_item_name : temp})
            
        except KeyError: # Print if the item does not exist in cart
            print(f"{item_name} does not exist in your cart")
        
    def update_item_qty(self, item_name, new_qty):
        '''
        Method to update item quantity in the shopping cart.
        
        update_item_qty(item_name, new_qty)
        
        Parameters:
        item_name = name of item, str
        new_qty   = new quantity, int
        '''
        try: # Update quantity if the item exists in cart
            self.cart[item_name][0] = new_qty
        
        except KeyError: # Print if the item does not exist in cart
            print(f"{item_name} does not exist in your cart")
    
    def update_item_price(self, item_name, new_price):
        '''
        Method to update item price in the shopping cart.
        
        update_item_price(item_name, new_price)
        
        Parameters:
        item_name = name of item, str
        new_price = new price, int
        '''
        try: # Update price if the item exists in cart
            self.cart[item_name][1] = new_price
            
        except KeyError: # Print if the item does not exist in cart
            print(f"{item_name} does not exist in your cart")
    
    def delete_item(self, item_name):
        '''
        Method to delete an item in the shopping cart.
        
        delete_item(item_name)
        
        Parameters:
        item_name = name of item to be deleted, str
        '''
        if len(self.cart) == 0:
            print("Cart is empty")
            return
        
        else:
            try: # Remove the item if it exists in cart
                self.cart.pop(item_name)
            except KeyError: # Print if the item does not exist in cart
                print(f"{item_name} does not exist in your cart")
        
    def reset_transaction(self):
        '''Clear all items in the cart.'''
        self.cart.clear()
    
    def check_order(self):
        '''Method to display all items in the shopping cart.'''
        if len(self.cart) == 0:
            print("Cart is empty")
            return
        
        else:
            df = pd.DataFrame(self.cart).T
            df["Item Name"] = df.index # Make index as usual column
            df = df[["Item Name",0,1,2]] # Rearrange columns
            new_index = [i for i in range(1, len(df)+1)] # Assign new index
            df.index = new_index
            df.columns = ["Item Name", "Quantity", "Price/Item", "Total Price/Item"]
            df.index.name = "No"
            print(df.to_markdown())
    
    def total_price(self):
        '''Method to display the total price of all items in cart and how much to pay'''
        list_keys = list(self.cart.keys())
        grand_total = 0
        
        for key in list_keys:
            grand_total += self.cart[key][2]
        
        if grand_total > 200000:
            print(f"Total price: Rp{grand_total}")
            amount_to_pay = 0.95*grand_total
            print("You are eligible to get 5% discount!")
            print(f"Amount to pay: Rp{amount_to_pay}")
        
        elif grand_total > 300000:
            print(f"Total price: Rp{grand_total}")
            amount_to_pay = 0.92*grand_total
            print("You are eligible to get 8% discount!")
            print(f"Amount to pay: Rp{amount_to_pay}")
        
        elif grand_total > 500000:
            print(f"Total price: Rp{grand_total}")
            amount_to_pay = 0.9*grand_total
            print("You are eligible to get 10% discount!")
            print(f"Amount to pay: Rp{amount_to_pay}")
        
        else:
            print(f"Amount to pay: Rp{grand_total}")
        