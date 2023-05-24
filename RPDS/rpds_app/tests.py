from django.test import TestCase
from .models import Contact

# Create your tests here.
class ContactFromTests(TestCase):
        .
    def test_create_contact_with_valid_email(self):
        """
        This function tests if a contact object can be created with a valid email address.
        """
        contact = Contact(email="test@example.com")
        assert contact.email == "test@example.com"