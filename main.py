import products
import store
import sys

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def list_all_products(best_buy):
    print("------")
    active_products = best_buy.get_all_products()
    for index, product in enumerate(active_products):
        print(f"{index + 1}. ", end="")
        product.show()
    print("------\n")


def show_total_amount(best_buy):
    total_amount = 0
    list_of_products = best_buy.get_all_products()
    for product in list_of_products:
        total_amount += product.get_quantity()
    print(f"Total of {total_amount} items in store\n")


def make_order(best_buy):
    list_all_products(best_buy)
    available_products = best_buy.get_all_products()
    print("When you want to finish order, enter empty text.")
    cart = []

    while True:
        product_choice = input("Which product # do you want? ").strip()
        if not product_choice:
            break
        if not product_choice.isdigit():
            print("Invalid input! Numeric value expected.")
            continue

        product_index = int(product_choice)
        if not (1 <= product_index <= len(available_products)):
            print("Invalid product number!")
            continue

        selected_product = available_products[product_index - 1]

        amount_input = input("What amount do you want? ").strip()
        if not amount_input.isdigit():
            print("Invalid input! Numeric value expected.")
            continue

        amount = int(amount_input)
        if not 0 < amount <= selected_product.get_quantity():
            print(f"Amount must be a number between 1 and the available stock of {selected_product.get_quantity()} units")
            continue

        cart.append((selected_product, amount))
        print("Product added to the shopping cart.")

    if not cart:
        return

    total_price = best_buy.order(cart)
    print(f"********\nOrder made! Total payment: ${total_price}\n")


def exit_program(best_buy):
    print("Thank you for your purchase!\n")
    sys.exit()


def start(best_buy):
    menu_functions = {
        1: list_all_products,
        2: show_total_amount,
        3: make_order,
        4: exit_program}

    print("Store Menu\n----------\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")
    try:
        function_of_choice = int(input("Please choose a number: "))
        if not isinstance(function_of_choice, int) or not function_of_choice in [1, 2, 3, 4]:
            raise KeyError
        menu_functions[function_of_choice](best_buy)

    except KeyError:
        print("Invalid input. Program expects a number from 1 to 4!")
        return start(best_buy)


def main():
    while True:
        start(best_buy)


if __name__ == "__main__":
    main()
