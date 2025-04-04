class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, product, quantity):
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")
        if product.name in self.cart:
            self.cart[product.name]['quantity'] += quantity
        else:
            self.cart[product.name] = {'price': product.price, 'quantity': quantity}
        product.stock -= quantity  # Decrease stock when added to the cart

    def remove_item(self, product, product_name):
        if product_name not in self.cart:
            raise KeyError(f"{product_name} not found in cart.")
        removed_quantity = self.cart[product_name]['quantity']
        del self.cart[product_name]
        
        # Restore the stock of the product correctly
        product.stock += removed_quantity  # Add the quantity back to stock
        
        # Correct the reference to the product and restore stock
        product = self.products[product_name]  # Get the product reference
        product.stock += removed_quantity  # Add the quantity back to stock

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\n--- Shopping Cart ---")
        for item, details in self.cart.items():
            print(f"{item}: {details['quantity']} x ${details['price']:.2f} = ${details['quantity'] * details['price']:.2f}")
        print("----------------------")

    def calculate_total(self):
        subtotal = sum(details['quantity'] * details['price'] for details in self.cart.values())
        tax = subtotal * 0.10  # 10% sales tax
        total = subtotal + tax
        return subtotal, tax, total

class POS:
    def __init__(self):
        self.products = {
            "Apple": Product("Apple", 100.00, 50),
            "Banana": Product("Banana", 300.00, 40),
            "Milk": Product("Milk", 580.00, 20),
            "Bread": Product("Bread", 500.00, 15),
            "Eggs": Product("Eggs", 1100.00, 30),
            "Rice": Product("Rice", 430.00, 12),
            "Bulla": Product("Bulla", 350.00, 8),
            "Butter": Product("Butter", 210.75, 12),
            "Tru Juice": Product("Tru Juice", 93.23, 25),
            "Frosted Flakes Cereal": Product("Frosted Flakes Cereal", 815.00, 6)
        }
        self.cart = ShoppingCart()

    def display_catalog(self):
        print("\n--- Product Catalog ---")
        for product in self.products.values():
            print(product)
        print("-----------------------")

    def process_transaction(self):
        while True:
            try:
                command = input("\nChoose an option:\n"
                                "1. Add\n"
                                "2. Remove\n"
                                "3. View Cart\n"
                                "4. Checkout\n"
                                "5. Exit\n"
                                "Enter your choice: ").strip().lower()

                if command == "add":
                    self.display_catalog()
                    product_name = input("Enter product name to add: ").strip().title()

                    if product_name not in self.products:
                        print("Product not found.")
                        continue  # Restart loop if product is not found

                    product = self.products[product_name]

                    if product.stock == 0:  # Check if the product is out of stock before asking for quantity
                        print(f"Sorry, {product_name} is out of stock.")
                        continue  # Skip asking for quantity if the product is out of stock

                    while True:  # Keep asking until a valid number is entered
                        try:
                            quantity = int(input("Enter quantity: "))
                            if quantity <= 0:
                                print("Quantity must be a positive number.")
                                continue  # Restart input loop
                            if quantity > product.stock:
                                print(f"Not enough stock for {product_name}. Available: {product.stock}")
                                continue  # Restart input loop

                            self.cart.add_item(product, quantity)
                            print(f"Added {quantity} x {product_name} to cart.")
                            break  # Exit loop when valid input is received

                        except ValueError:
                            print("Invalid input. Please enter a valid number for quantity.")

                elif command == "remove":
                    product_name = input("Enter product name to remove: ").strip().title()
                    if product_name in self.products:
                        product = self.products[product_name]
                        self.cart.remove_item(product, product_name)
                        print(f"Removed {product_name} from cart.")
                    else:
                        print(f"{product_name} not found.")

                elif command in ["view", "cart", "view cart"]:
                    self.cart.view_cart()

                elif command == "checkout":
                    self.checkout()
                    break

                elif command == "exit":
                    print("Exiting transaction...")
                    break

                else:
                    print("Invalid command. Please try again.")

            except Exception as e:  # Ensure there is an 'except' block to catch errors
                print(f"Error: {e}")

    def checkout(self):
        subtotal, tax, total = self.cart.calculate_total()
        print("\n--- Checkout ---")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        if total > 5000:
            discount = total * 0.05
            total -= discount
            print(f"Discount (5%): ${discount:.2f}")
            print(f"New Total: ${total:.2f}")
        while True:
            try:
                payment = float(input("Enter amount received: $"))
                if payment < total:
                    raise ValueError("Insufficient balance.")
                change = payment - total
                self.generate_receipt(subtotal, tax, total, payment, change)
                break
            except ValueError as ve:
                print(f"Error: {ve}")

    def generate_receipt(self, subtotal, tax, total, payment, change):
        print("\n--- Receipt ---")
        print("Best Buy Retail Store")
        print("=====================")
        self.cart.view_cart()
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Payment: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        print("\nThank You for Shopping with Us! Enjoy your day!")
        print("-----------------")

    def check_low_stock(self):
        for product in self.products.values():
            if product.stock < 5:
                print(f"{product.name} is low on stock ({product.stock} left).")

    def reset_cart(self):
        self.cart = ShoppingCart()  # Reset cart for a new transaction


def main():
    pos = POS()
    while True:
        print("\nWelcome to Best Buy Retail Store POS System")
        pos.process_transaction()
        pos.check_low_stock()

        while True:  # Loop until a valid response is given
            another_transaction = input("\nStart another transaction? (yes/no): ").strip().lower()

            if another_transaction == "yes":
                pos.reset_cart()  # Reset the cart when starting a new transaction
                break  # Restart the transaction loop

            elif another_transaction == "no":
                print("Thank you for using the POS system. Goodbye!")
                exit()  # Exit the program

            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()
“I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT”