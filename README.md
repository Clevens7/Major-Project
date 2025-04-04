Authors: Catherine Salkey & Clevens Denton
Date Created: April 2, 2025
Course: ITT 103
Git Hub Public Code to URL: 


The purpose of the Better Buy POS Program:
The program aims to be a Point of Sale (POS) System. It simulates a real-world instance showcasing the practicality of object-
oriented programming (OOP), modular design, and exception handling. This POS system is one that will allow cashiers of the Better 
Buy grocery store to process customer purchases. The system has a simple interface where in which cashiers can add items to a shopping cart,
remove items, view the cart, calculate the total bill (inclusive of tax and applied discounts), accept payment, generate a receipt and keep 
track of stock. 

How to run it:
1. Upon opening the program, the user will greeted by the main menu and will be prompted to type out their selected action. ( Type: "add", "remove", "view", "checkout", "exit")
2. When that is done, a predefined product catalog with the product names, prices, and stock quantities will be displayed.
3. After, the user will be asked to input the product name and quantity of the product they would like to purchase.
4. The user will then be presented with the menu again to either add more items, remove an item, view their cart, checkout etc.

Shopping Cart Operations:

A. Add Operation
• If the user adds more items, the stocks of those particular items will be updated immediately for users to see how much remains.
• The program will ensure that the system validates stock availability before adding items to the cart. 
• It will also show an alert when the stock of any item falls below 5.

B. Remove operaton
 • After adding an item to the cart, the user has the ability to remove any item that was recently added to the cart before checking out.

C. Provide an option to view the cart with a list of items, their quantities, and their total price.

Checkout & Payment Processing: This option calculate the subtotal of all items in the cart when the user inputs checkout. 
• Upon checking out, a 10% sales tax will be applied to the subtotal and the new total will display the total amount due.
• The program will allow the cashier to enter the amount received from the customer and calculate the change. 
• Ensure that the system validates payment (i.e., customer cannot pay less than the total amount due).
• Applies a 5% discount on any bills over $5000.


Receipt Generation
Generates a formatted receipt displaying: 
 • Store name and a header. 
 • Itemised list of purchased items with quantity, unit price, and total price. 
 • The subtotal, sales tax, and total amount due. 
 • The amount paid by the customer and the change returned. 
 • A “Thank You” message at the end of the receipt.

Allow multiple transactions to take place in a single session by asking users a question before they exit.

Required Modifications:
 • The program can be modified by chaging the name in the header of the receipt to an actual business.
 • The catalougue can be modified with new items and prices.
 • The sales tax and dicount.
 • The reciept design/format.

Limitations of its operation:
 • Can't easily add products from the outside.
 • The system in limited to a hard coded catalougue it runs off of. If a new item is on shelves or the prices of goods change, one has to modify the code for it to work correctly.
 • If an item is accidently excluded, one has to modify the code to add that product.
