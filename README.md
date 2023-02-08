# Simple Cashier Program
This project demonstrates a simple program with several basic operations that are necessary to register items at the cashier. The program is built mainly as function and object based program using Python (OOP). More details about this program will be further discussed in this documentation.

---

## Background
A program is needed for a cash register at a self-service supermarket. Using this program, users are able to input their membership ID, add, delete, and modify the name, quantity, and price of items they want to buy. The program can also show a list of items in their shopping cart, and calculate the discounts that the customers can get based on their total spending.

## Requirements
- Customers can input their ID.
- Customers can input the item name, quantity, and price.
- Customers can modify the item name, quantity, and price.
- Customers can delete item name, quantity, and price.
- Customers can reset items their shopping cart.
- Customers can check their orders.
- The program can calculate the total price, including discounts.

## Flowchart
![Flowchart](pics/flowchart_cashier.png "Flowchart")

The program first prompts the user to input their customer or membership ID. After that, it expects users to choose menu or operations to take by inputting a number that corresponds to the menu itself:
1. Add item
2. Delete item
3. Update item name
4. Update item quantity
5. Update item price
6. Check order
7. Display total price
8. Reset shopping cart
0. Exit

After an operation is done, the program will ask whether the user wants to end shopping or the continue with other operation. If the user wants to continue with other operations, the program will again ask which menu or operation to take. If the user wants to end shopping, it quits the loop and display order details and price to pay.
