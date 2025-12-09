class Store:
    """Represents a store that holds multiple products."""

    def __init__(self, products_list):
        """
        Initialize the store with a list of products.

        :param products_list: list of Product instances
        """
        # we make a copy so external code cannot modify our internal list directly
        self.products = list(products_list)

    # ---------- product management ----------

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    # ---------- information / queries ----------

    def get_total_quantity(self):
        """
        Return the total quantity of all products in the store.

        This is the sum of the quantities of every product.
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Return a list of all *active* products in the store.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    # ---------- ordering ----------

    def order(self, shopping_list):
        """
        Receive a list of (product, quantity) tuples and buy them.

        :param shopping_list: list of tuples (Product, int)
        :return: total price of the order as float
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            # Verwende self -> Produkt muss im Store sein
            if product not in self.products:
                raise ValueError("Product not found in store.")

            total_price += product.buy(quantity)

        return total_price