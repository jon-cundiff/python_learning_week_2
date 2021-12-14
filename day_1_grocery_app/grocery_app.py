from typing import final
import shopping_list
import address
import grocery_item
import util

shopping_lists = []

while True:
    print("==============================")
    print(" 1. Add a New Shopping List")
    print(" 2. Add Item to Existing List")
    print(" 3. Display Shopping Lists")
    print(" 4. Remove Item in Shopping List")
    print(" 5. Remove Shopping List")
    print(" q to quit")
    print("==============================")
    choice = input("Please select an option: ")

    try:
        # Add new shopping list
        if choice == "1":
            title = input("\nWhat is the name of the store? ")
            (street, city, state, zip_code) = util.gather_address_info()

            shop_address = address.Address(street, city, state, zip_code)
            shop_list = shopping_list.ShoppingList(title, shop_address)
            shopping_lists.append(shop_list)
            util.display_lists(shopping_lists)

        # Add item to shopping list
        elif choice == "2":
            if len(shopping_lists) > 0:
                util.display_list_titles(shopping_lists)
                list_choice = int(
                    input("Select shopping list to add an item to: "))

                shop_list = shopping_lists[list_choice - 1]
                (title, price, quantity) = util.gather_grocery_item_info(
                    shop_list.title)

                shop_list.add_grocery_item(
                    grocery_item.GroceryItem(title, price, quantity))

                shop_list.display_list()

            else:
                print("No shopping lists.")

        # Display Shopping Lists
        elif choice == "3":
            if len(shopping_lists) > 0:
                util.display_lists(shopping_lists)
            else:
                print("No shopping lists")

        # Remove item from shopping list
        elif choice == "4":
            if len(shopping_lists) > 0:
                util.display_list_titles(shopping_lists)
                list_choice = int(
                    input("Select shopping list to remove an item from: "))

                shop_list = shopping_lists[list_choice - 1]
                if len(shop_list.grocery_items) > 0:
                    shop_list.display_list(True)
                    item_to_remove = int(
                        input("Select an item to remove: "))
                    shop_list.remove_grocery_item(item_to_remove - 1)
                    util.display_lists(shopping_lists)
                else:
                    print(f"{shop_list.title} has no items")

            else:
                print("No shopping lists")

        # Remove shopping list
        elif choice == "5":
            if len(shopping_lists) > 0:
                util.display_list_titles(shopping_lists)
                list_choice = int(
                    input("Select shopping list to remove: "))

                del shopping_lists[list_choice - 1]
                util.display_lists(shopping_lists)
            else:
                print("No shopping lists")

        # Quit program
        elif choice.lower() == "q":
            break
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")

    except IndexError:
        print("Item not found.")
    # New Line between loops
    finally:
        print('')
