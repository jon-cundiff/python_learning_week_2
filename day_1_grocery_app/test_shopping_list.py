import unittest
import sys
import io
import shopping_list as sl
import grocery_item as gi
import address as addr

test_items = [
    gi.GroceryItem("Eggs", 4.50, 12),
    gi.GroceryItem("Milk", 4.50, 1)
]


class ShoppingListTest(unittest.TestCase):
    def setUp(self):
        address = addr.Address("123 Test St", "Kansas City", "MO", "64080")
        self.shopping_list = sl.ShoppingList("Walmart", address)
        self.shopping_list.grocery_items

    def test_can_add_item(self):
        self.shopping_list.add_grocery_item(test_items[0])
        self.assertEqual(1, len(self.shopping_list.grocery_items))

    def test_cannot_add_duplicate_item(self):
        self.shopping_list.add_grocery_item(test_items[0])
        self.shopping_list.add_grocery_item(test_items[0])
        self.assertEqual(1, len(self.shopping_list.grocery_items))

    def test_can_remove_item(self):
        self.shopping_list.add_grocery_item(test_items[0])
        self.shopping_list.remove_grocery_item(0)
        self.assertEqual([], self.shopping_list.grocery_items)

    def test_can_display_no_items(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.shopping_list.display_list()
        sys.stdout = sys.__stdout__

        expected_string = "\n***** Walmart *****\n  -- No Items --\n"
        self.assertEqual(expected_string, capturedOutput.getvalue())

    def test_can_display_csv_items(self):
        self.shopping_list.add_grocery_item(test_items[0])
        self.shopping_list.add_grocery_item(test_items[1])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.shopping_list.display_list()
        sys.stdout = sys.__stdout__

        expected_string = "\n***** Walmart *****\n  +  Eggs, Milk\n"
        self.assertEqual(expected_string, capturedOutput.getvalue())

    def test_can_display_numbered_items(self):
        self.shopping_list.add_grocery_item(test_items[0])
        self.shopping_list.add_grocery_item(test_items[1])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.shopping_list.display_list(True)
        sys.stdout = sys.__stdout__

        expected_string = "\n***** Walmart *****\n  1 - Eggs\n  2 - Milk\n"
        self.assertEqual(expected_string, capturedOutput.getvalue())


unittest.main()
