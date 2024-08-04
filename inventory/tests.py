import unittest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from inventory.models import Product, Inventory, Sale

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = User.objects.create_user(username='willivamtest', password='test1234')
        cls.token = RefreshToken.for_user(cls.user)
        cls.access_token = str(cls.token.access_token)

        cls.product = Product.objects.create(name="Test Product", price=10.99, description="Test Description")
        cls.inventory = Inventory.objects.create(product=cls.product, quantity=100, warehouse="Main Warehouse")

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the API home page tecnical test "})

    def test_create_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "name": "New Product",
            "price": "20.99",
            "description": "New Product Description"
        }
        response = self.client.post(reverse('product'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Product registered")

    def test_update_product(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "price": "15.99"
        }
        url = reverse('update_product', args=[self.product.id])
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Product updated")

    def test_create_inventory(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "product": self.product.id,
            "quantity": 50,
            "warehouse": "New Warehouse"
        }
        response = self.client.post(reverse('inventory'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Inventory registered/updated")

    def test_create_sale(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        data = {
            "product_id": self.inventory.product.id,
            "quantity": 10,
            "warehouse": self.inventory.warehouse
        }
        response = self.client.post(reverse('sale'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Sale registered")

    def test_sales_report(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('sales_report'))
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
