def gather_address_info():
    street = input("What is the street address? ")
    city = input("What is the city? ")
    state = input("What state is it in? ")
    zip_code = input("What is the zip code? ")
    return (street, city, state, zip_code)


def gather_grocery_item_info(shopping_list_title):
    title = input(
        f"What item would you like to add to {shopping_list_title}? ")
    price = int(input("How much does each cost? "))
    quantity = int(input("How many do you need to buy? "))
    return (title, price, quantity)


def display_list_titles(shopping_lists):
    print('\n***** SHOPPING LISTS *****')
    for index in range(len(shopping_lists)):
        print(f" {index + 1} - {shopping_lists[index].title}")
    print('**************************')


def display_lists(shopping_lists):
    for shopping_list in shopping_lists:
        shopping_list.display_list()
