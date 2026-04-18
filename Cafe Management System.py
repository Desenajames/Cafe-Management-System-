
import datetime

class Cafe:
    def __init__(self):
    
        self.menu = {
            "coffee": 2.50,
            "cookie": 2.00,
            "sandwich": 5.00,
            "cake": 3.50,
            "lemonade": 2.80
        }
        self.order = {}

    def display_menu(self):
        print("\n====================================")
        print("   Welcome to Our Cafe ☕")
        print("====================================")
        print("Here is our menu (prices in €):\n")
        for item, price in self.menu.items():
            print(f"- {item:<10} : €{price:.2f}")
        print("====================================\n")

    def take_order(self):
        while True:
            item = input("Enter item name: ").title()

            if item not in self.menu:
                print("❌ Item not available. Please choose from the menu.")
                continue

            try:
                quantity = int(input(f"Enter quantity for {item}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            except ValueError:
                print("❌ Enter a valid number.")
                continue

            if item in self.order:
                self.order[item] += quantity
            else:
                self.order[item] = quantity

            more = input("Would you like to order more? (yes/no): ").lower()
            if more != "yes":
                break

    def calculate_total(self):
        total = 0
        for item, quantity in self.order.items():
            total += self.menu[item] * quantity
        return total

    def print_receipt(self, total):
        now = datetime.datetime.now()
        print("\n============= RECEIPT =============")
        print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-----------------------------------")
        for item, quantity in self.order.items():
            item_total = self.menu[item] * quantity
            print(f"{item:<10} x{quantity:<2} = €{item_total:.2f}")
        print("-----------------------------------")
        print(f"TOTAL: €{total:.2f}")
        print("===================================")

def main():
    cafe = Cafe()
    cafe.display_menu()
    cafe.take_order()

    if not cafe.order:
        print("No items ordered.")
        print("Thank you for visiting our cafe! ☕")
        return

    total = cafe.calculate_total()

    
    print(f"\nYour total amount is: €{total:.2f}")

    
    choice = input("Do you want to print the receipt? (yes/no): ").lower()
    if choice == "yes":
        cafe.print_receipt(total)

    
    print("\nThank you for visiting our cafe! ☕")

if __name__ == "__main__":
    main()