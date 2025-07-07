# The beginning of the class
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (
            f"Country: {self.country}, Code: {self.code}, "
            f"Product: {self.product}, Cost: R {self.cost:.2f}, "
            f"Quantity: {self.quantity}"
        )


# Shoe list=
shoe_list = []


# Functions outside the class
def read_shoes_data():
    try:
        with open("inventory.py", "r", encoding="utf-8") as file:
            next(file)
            for line in file:
                if line.strip():
                    country, code, product, cost, quantity = (
                        line.strip().split(",")
                    )
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
        print("Inventory data loaded successfully.\n")
    except FileNotFoundError:
        print("Error: inventory.py not found.\n")
    except ValueError:
        print("Error: One or more lines in the file are incorrectly formatted.\n")


def capture_shoes():
    country = input("Please enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print("Shoe captured successfully.\n")


def view_all():
    if shoe_list:
        for shoe in shoe_list:
            print(shoe)
    else:
        print("No shoe data available.\n")


def re_stock():
    if not shoe_list:
        print("No inventory loaded.\n")
        return

    lowest = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Lowest stock shoe: {lowest}")
    try:
        add_qty = int(input(f"Enter quantity to add to {lowest.product}: "))
        lowest.quantity += add_qty
        update_inventory_file()
        print("Stock updated successfully.\n")
    except ValueError:
        print("Invalid quantity.\n")


def search_shoe():
    search_code = input("Enter product code to search: ").strip()
    found = False
    for shoe in shoe_list:
        if shoe.code == search_code:
            print(f"\nShoe found:\n{shoe}\n")
            found = True
            break
    if not found:
        print("Shoe not found.\n")


def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} - Total Value: R{value:,.2f}")


def highest_qty():
    if not shoe_list:
        print("No inventory loaded.\n")
        return

    highest = max(shoe_list, key=lambda x: x.get_quantity())
    print(
        f"{highest.product} is for sale! "
        f"({highest.quantity} units available)\n"
    )


def update_inventory_file():
    with open("inventory.py", "w", encoding="utf-8") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},"
                f"{shoe.cost},{shoe.quantity}\n"
            )


# Main Menu=
def main():
    read_shoes_data()
    while True:
        print("\n==== Shoe Inventory Menu ====")
        print("1. View all shoes")
        print("2. Capture new shoes")
        print("3. Restock shoes")
        print("4. Search shoe by code")
        print("5. Calculate the value per item")
        print("6. Identify the highest quantity (for sale)")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
