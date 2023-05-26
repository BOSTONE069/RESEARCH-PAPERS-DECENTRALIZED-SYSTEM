from django.test import TestCase
from .models import Contact
from datetime import datetime
# Create your tests here.

class ContactTests(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(name='John Doe', email='john@mail.com')

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'John Doe')
        self.assertEqual(self.contact.email, 'john@mail.com')
        self.assertIsInstance(self.contact.created_at, datetime)

    def test_string_representation(self):
        self.assertEqual(str(self.contact), 'john@mail.com John Doe {}'.format(self.contact.created_at))

        
