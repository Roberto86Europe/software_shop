class Product:
    """
    Represents a product in the warehouse.

    Attributes:
        name (str): The name of the product.
        quantity (int): The available quantity of the product.
        sale_price (float): The sale price of the product.
        purchase_price (float): The purchase price of the product.
    """

    def __init__(self, name, quantity, sale_price, purchase_price):
        """
        Initializes a new Product object.

        Args:
            name (str): The name of the product.
            quantity (int): The available quantity of the product.
            sale_price (float): The sale price of the product.
            purchase_price (float): The purchase price of the product.
        """
        self.name = name
        self.quantity = quantity
        self.sale_price = sale_price
        self.purchase_price = purchase_price
    
    def is_available(self):
        """
        Checks if the product is available.

        Returns:
            bool: True if the product is available, False otherwise.
        """
        return self.quantity > 0

    def validate_quantity(self, quantity):
        """
        Validate the quantity input.

        Args:
            quantity (str): The quantity input value.

        Returns:
            int: The validated quantity if it is a positive integer, 0 otherwise.

        """
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Error: Quantità deve essere un numero positivo.")
                return None
            return quantity
        except ValueError:
            print(f"Error: Il valore della '{quantity}' deve essere un numero intero.")
            return None

    def validate_price(self, price):
        """
        Validate the price input and return a float value.

        Args:
            price (str): The price input value.

        Returns:
            float: The validated price as a float, or None if the value is not a valid float or negative.

        """
        try:
            price = float(price)
            if price < 0:
                print("Error: Il prezzo non può essere negativo.")
                return None
            return price
        except ValueError:
            print(f"Error: inserisci il'{price}' correttamente .")
            return None


# Initialize products dictionary
products = {}

# Define the loop for the program
cmd = None
while cmd != "chiudi":
    cmd = input("Inserisci un comando: ")

    if cmd == "aiuto":
        print("I comandi disponibili sono i seguenti:\n"
              "- aggiungi: aggiungi un prodotto al magazzino\n"
              "- elenca: elenca i prodotto in magazzino\n"
              "- vendita: registra una vendita effettuata\n"
              "- profitti: mostra i profitti totali\n"
              "- aiuto: mostra i possibili comandi\n"
              "- chiudi: esci dal programma")
    elif cmd == "aggiungi":
        # Get product details from user input
        name = input("Nome del prodotto: ")
        quantity = input("Quantità: ")
        
        product = Product(name, 0, 0, 0)  # Create an instance of Product
        quantity = product.validate_quantity(quantity)  # Call validate_quantity on the instance
        
        if quantity is None:
            continue  # Skip the rest of the loop if quantity is None or invalid
        buy_price = input("Prezzo di acquisto: ")
        buy_price = product.validate_price(buy_price)  # Call validate_price on the instance
        if buy_price is None:
            continue  # Skip the rest of the loop if buy_price is None or invalid
        sell_price = input("Prezzo di vendita: ")
        sell_price = product.validate_price(sell_price)  # Call validate_price on the instance
        if sell_price is None:
            continue  # Skip the rest of the loop if sell_price is None or invalid




        # Add product to dictionary
        products[name] = {"quantita": quantity,
                          "prezzo_acquisto": buy_price,
                          "prezzo_vendita": sell_price}
        print(f"AGGIUNTO: {quantity} X {name}")
    
    elif cmd == "elenca":
        # Print table of products and their details
        print("PRODUCT QUANTITY PRICE")
        for name, details in products.items():
            if details['quantita'] > 0:
                print(f"{name} {details['quantita']} €{details['prezzo_vendita']}")

    elif cmd == "vendita":
        # Initialize variables for the sale
        sale_total = 0
        sale_profit = 0
        sale_details = {}

        while True:
            # Get product details from user input
            name = input("Nome del prodotto: ")
            if name not in products:
                print("Prodotto non trovato")
                continue

            quantity = int(input("Quantità: "))
            if quantity > products[name]["quantita"]:
                print("Quantità insufficiente")
                continue

            # Calculate sale total and profit
            sale_total += quantity * products[name]["prezzo_vendita"]
            sale_profit += quantity * (products[name]["prezzo_vendita"] - products[name]["prezzo_acquisto"])

            # Update product quantity
            products[name]["quantita"] -= quantity

            # Add product to sale details
            if name in sale_details:
                sale_details[name] += quantity
            else:
                sale_details[name] = quantity

            # Ask user if they want to add another product to the sale
            another = input("Aggiungere un altro prodotto? (si/no): ")
            if another.lower() == "no":
                break

        # Print sale details
        print("VENDITA REGISTRATA")
        for name, quantity in sale_details.items():
            print(f"- {quantity} X {name}: €{products[name]['prezzo_vendita']}")
        print(f"Totale: €{sale_total:.2f}")
    
    elif cmd == "profitti":
        # Calculate total profit
        total_profit = sum([details["quantita"] * (details["prezzo_vendita"] ) for details in products.values()])
        net_profit = total_profit * 0.45
        print(f"Profitto: lordo=€{total_profit:.2f} netto=€{net_profit:.2f}")

    elif cmd == "chiudi":
        print("Bye bye")
    else:
        print("Comando non valido\n"
              "I comandi disponibili sono i seguenti:\n"
              "- aggiungi: aggiungi un prodotto al magazzino\n"
              "- elenca: elenca i prodotto in magazzino\n"
              "- vendita: registra una vendita effettuata\n"
              "- profitti: mostra i profitti totali\n"
              "- aiuto: mostra i possibili comandi\n"
              "- chiudi: esci dal programma\n")
