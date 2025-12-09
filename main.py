import products
import store


def list_products(store_obj):
    """Print all active products in the store with an index."""
    products_list = store_obj.get_all_products()

    if not products_list:
        print("No active products in store.")
        return

    print("\n--- Products in store ---")
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. ", end="")
        product.show()
    print("-------------------------")


def show_total_amount(store_obj):
    """Print the total quantity of items in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal quantity in store: {total_quantity}\n")


def make_order(store_obj):
    """Interactively create an order and place it in the store."""
    products_list = store_obj.get_all_products()

    if not products_list:
        print("No active products available for ordering.")
        return

    # Show products so the user can select by index
    list_products(store_obj)

    shopping_list = []

    while True:
        product_input = input(
            "Enter product number to add to order "
            "(or press Enter to finish): "
        )

        if product_input.strip() == "":
            break

        try:
            product_index = int(product_input)
            if not 1 <= product_index <= len(products_list):
                print("Invalid product number. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        quantity_input = input("Enter quantity: ")

        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Quantity must be positive. Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer quantity.")
            continue

        product = products_list[product_index - 1]
        shopping_list.append((product, quantity))
        print("Item added to order.\n")

    if not shopping_list:
        print("No items selected. Order cancelled.\n")
        return

    try:
        total_price = store_obj.order(shopping_list)
        print(f"\nOrder placed successfully! Total price: {total_price}\n")
    except Exception as error:  # relies on Product.buy raising exceptions
        print(f"\nError while placing order: {error}\n")


def start(store_obj):
    """
    Start the user interface loop for the store.

    Shows a menu and reacts to the user's choices.
    """
    while True:
        print("Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Your choice: ").strip()
        print()

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


def main():
    """Set up initial inventory and start the user interface."""
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)

    # start the menu-based user interface
    start(best_buy)


if __name__ == "__main__":
    main()
