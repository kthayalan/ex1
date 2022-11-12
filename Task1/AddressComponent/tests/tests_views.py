from rest_framework.test import APITestCase, APIClient


class AddressTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_address(self):
        pass
