class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.grocery_items = []

    def add_grocery_item(self, item):
        self.grocery_items.append(item)

    def remove_grocery_item(self, item_to_remove):
        if item_to_remove >= 0 and item_to_remove < len(self.grocery_items):
            del self.grocery_items[item_to_remove]
        else:
            print("Invalid Index")

    def convert_grocery_items_titles_to_CSV(self):
        grocery_item_titles = []
        for grocery_item in self.grocery_items:
            grocery_item_titles.append(grocery_item.title)

        return ", ".join(grocery_item_titles)

    def convert_grocery_items_titles_to_numbered_list(self):
        grocery_item_titles = []
        for index in range(len(self.grocery_items)):
            line_message = f"  {index + 1} - {self.grocery_items[index].title}"
            grocery_item_titles.append(line_message)

        return "\n".join(grocery_item_titles)

    def display_list(self, expanded=False):
        print(f"\n***** {self.title} *****")
        message = ""
        if len(self.grocery_items) > 0:
            if expanded:
                message = self.convert_grocery_items_titles_to_numbered_list()
            else:
                message = "  +  " + self.convert_grocery_items_titles_to_CSV()
        else:
            message = "  -- No Items -- "
        print(message)
