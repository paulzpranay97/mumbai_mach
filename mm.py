import json

def load_data():
    try:
        with open('snacks_data.json', 'r') as file:
            snacks_data = json.load(file)
    except FileNotFoundError:
        snacks_data = []
    return snacks_data

def save_data(snacks_data):
    with open('snacks_data.json', 'w') as file:
        json.dump(snacks_data, file)

def add_item(item_name, item_price, item_quantity):
    snacks_data = load_data()
    item = {
        'name': item_name,
        'price': item_price,
        'quantity': item_quantity
    }
    snacks_data.append(item)
    save_data(snacks_data)

def get_all_items():
    return load_data()

def update_item(name, new_price=None, new_quantity=None):
    snacks_data = load_data()
    for item in snacks_data:
        if item['name'] == name:
            if new_price is not None:
                item['price'] = new_price
            if new_quantity is not None:
                item['quantity'] = new_quantity
            save_data(snacks_data)
            break

def delete_item(name):
    snacks_data = load_data()
    snacks_data = [item for item in snacks_data if item['name'] != name]
    save_data(snacks_data)

if __name__ == "__main__":
    while True:
        print("1. Add an item")
        print("2. View all items")
        print("3. Update an item")
        print("4. Delete an item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the price: "))
            item_quantity = int(input("Enter the quantity: "))
            add_item(item_name, item_price, item_quantity)
        elif choice == '2':
            all_items = get_all_items()
            for item in all_items:
                print(f"{item['name']} - Price: ${item['price']}, Quantity: {item['quantity']}")
        elif choice == '3':
            item_name = input("Enter the item name to update: ")
            new_price = float(input("Enter the new price (press Enter to skip): ") or None)
            new_quantity = int(input("Enter the new quantity (press Enter to skip): ") or None)
            update_item(item_name, new_price, new_quantity)
        elif choice == '4':
            item_name = input("Enter the item name to delete: ")
            delete_item(item_name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
