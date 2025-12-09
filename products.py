class Product:
    """Represents a product type that is available in the store."""

    def __init__(self, name, price, quantity):
        """
        Initialize a new product.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # ---------- Quantity / active handling ----------

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set a new quantity for the product.

        If the quantity becomes zero, the product is deactivated.
        """
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            # Optional: ensure the product is active again when quantity > 0
            self.activate()

    def is_active(self):
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    # ---------- Display and buying ----------

    def show(self):
        """Print a string representation of the product."""
        print(
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        )

    def buy(self, quantity):
        """
        Buy a certain quantity of the product.

        Returns the total price of the purchase.

        Raises an exception if:
        - the product is not active
        - the requested quantity is not positive
        - there is not enough quantity in stock
        """
        if not self.active:
            raise ValueError("Cannot buy an inactive product.")

        if quantity <= 0:
            raise ValueError("Quantity to buy must be positive.")

        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price



