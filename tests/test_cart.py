import unittest
from cart import ShoppingCart


def cart_with_items(*items):
    """Build a cart from tuples of (name, price, quantity)."""
    cart = ShoppingCart()
    for name, price, quantity in items:
        cart.add_item(name, price, quantity)
    return cart


class TestShoppingCart(unittest.TestCase):
    def test_add_item_updates_total(self):
        cart = ShoppingCart()
        cart.add_item("apple", 1.50, 4)
        cart.add_item("banana", 0.50, 2)
        self.assertEqual(cart.get_total(), 7.00)

    def test_add_item_existing_name_accumulates_quantity(self):
        cart = ShoppingCart()
        cart.add_item("apple", 2.00, 2)
        cart.add_item("apple", 2.00, 3)
        self.assertEqual(cart.get_item_count(), 5)
        self.assertEqual(cart.get_total(), 10.00)

    def test_add_item_rejects_zero_quantity(self):
        cart = ShoppingCart()
        with self.assertRaises(ValueError):
            cart.add_item("apple", 1.50, 0)

    def test_remove_existing_item(self):
        cart = cart_with_items(("apple", 1.00, 3), ("milk", 2.00, 1))
        cart.remove_item("apple")
        self.assertEqual(cart.get_total(), 2.00)

    def test_remove_non_existing_item_raises_key_error(self):
        cart = ShoppingCart()
        with self.assertRaises(KeyError):
            cart.remove_item("ghost_item")

    def test_save10_discount_reduces_total_by_10_percent(self):
        cart = cart_with_items(("item", 100.00, 1))
        cart.apply_discount("SAVE10")
        self.assertEqual(cart.get_total(), 90.00)

    def test_save20_discount_is_allowed_at_exact_threshold(self):
        cart = cart_with_items(("item", 50.00, 1))
        cart.apply_discount("SAVE20")
        self.assertEqual(cart.get_total(), 40.00)

    def test_flat5_discount_is_allowed_at_exact_threshold(self):
        cart = cart_with_items(("item", 30.00, 1))
        cart.apply_discount("FLAT5")
        self.assertEqual(cart.get_total(), 25.00)

    def test_clear_empties_cart(self):
        cart = cart_with_items(("apple", 2.00, 5))
        cart.clear()
        self.assertEqual(cart.get_total(), 0.00)

    def test_get_item_count_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.get_item_count(), 0)

    def test_get_item_count_returns_sum_of_quantities(self):
        cart = cart_with_items(
            ("apple", 1.00, 3),
            ("banana", 0.50, 2),
            ("mango", 2.00, 5),
        )
        self.assertEqual(cart.get_item_count(), 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
