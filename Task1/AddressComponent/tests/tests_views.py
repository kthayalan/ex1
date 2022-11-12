from rest_framework.test import APITestCase, APIClient
from AddressComponent.models import Address
from rest_framework.response import Response

class AddressTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_address(self):
        add = Address.Objects.all()
        return Response(add)
