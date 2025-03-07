import unittest
from service.models import Product
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    """Test CRUD operations on the Product model"""

    def test_create_product(self):
        product = ProductFactory()
        self.assertIsNotNone(product)
    
    def test_read_product(self):
        product = ProductFactory()
        self.assertEqual(Product.find(product.id).id, product.id)

    def test_update_product(self):
        product = ProductFactory()
        product.name = "Updated Name"
        product.update()
        self.assertEqual(Product.find(product.id).name, "Updated Name")

    def test_delete_product(self):
        product = ProductFactory()
        product.delete()
        self.assertIsNone(Product.find(product.id))

    def test_list_all_products(self):
        ProductFactory.create_batch(3)
        self.assertEqual(len(Product.all()), 3)

    def test_find_by_name(self):
        product = ProductFactory(name="Laptop")
        self.assertEqual(Product.find_by_name("Laptop").first().name, "Laptop")

    def test_find_by_category(self):
        product = ProductFactory(category="Electronics")
        self.assertEqual(Product.find_by_category("Electronics").first().category, "Electronics")

    def test_find_by_availability(self):
        product = ProductFactory(available=True)
        self.assertTrue(Product.find_by_availability(True).first().available)
