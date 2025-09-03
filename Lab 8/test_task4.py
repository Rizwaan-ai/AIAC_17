import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def test_add_multiple_different_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.5)
        cart.add_item("banana", 1.0)
        self.assertEqual(cart.items["apple"]["quantity"], 1)
        self.assertEqual(cart.items["banana"]["quantity"], 1)
        self.assertEqual(cart.items["apple"]["price"], 2.5)
        self.assertEqual(cart.items["banana"]["price"], 1.0)

    def test_add_item_with_different_price(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.5)
        cart.add_item("apple", 3.0)
        # Should keep original price
        self.assertEqual(cart.items["apple"]["price"], 2.5)
        self.assertEqual(cart.items["apple"]["quantity"], 2)

    def test_remove_item_until_empty(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.5)
        cart.remove_item("apple")
        self.assertNotIn("apple", cart.items)

    def test_total_cost_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total_cost(), 0)

    def test_show_cart_empty(self):
        cart = ShoppingCart()
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        cart.show_cart()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "")

    def test_add_and_remove_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.0)
        cart.add_item("banana", 1.0)
        cart.add_item("apple", 2.0)
        cart.remove_item("apple")
        self.assertEqual(cart.items["apple"]["quantity"], 1)
        self.assertIn("banana", cart.items)

    def test_remove_item_not_present(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.0)
        cart.remove_item("banana")  # Should not raise
        self.assertIn("apple", cart.items)
        self.assertNotIn("banana", cart.items)

if __name__ == "__main__":
    unittest.main()