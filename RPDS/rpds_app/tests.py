from django.test import TestCase, Client
from .models import Contact
from datetime import datetime
from .forms import ContactForm
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

# The ContactTests class tests the creation and string representation of a Contact object.
class ContactTests(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(name='John Doe', email='john@mail.com')

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'John Doe')
        self.assertEqual(self.contact.email, 'john@mail.com')
        self.assertIsInstance(self.contact.created_at, datetime)

    def test_string_representation(self):
        self.assertEqual(str(self.contact), 'john@mail.com John Doe {}'.format(self.contact.created_at))

# This is a test case for a Django view that tests whether the view uses a contact form, saves data
# for valid form submission, and does not save data for invalid form submission.
class ContactViewTestCase(TestCase):
     def setUp(self):
        self.url = reverse('contact')
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john@example.com'
        }

     def test_contact_view_should_use_contact_form(self):
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], ContactForm)

     def test_contact_view_should_save_data_for_valid_form_submission(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().name, 'John Doe')
        self.assertEqual(Contact.objects.first().email, 'john@example.com')
        self.assertRedirects(response, reverse('success'))

     def test_contact_view_should_not_save_data_for_invalid_form_submission(self):
        invalid_data = {
            'name': 'John Doe',
            'email': 'invalid-email'
        }
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(Contact.objects.count(), 0)
        self.assertContains(response, 'Enter a valid email address.')


# This is a test case for a successful login process in Django, which creates a test user and checks
# if the user is redirected to the correct page and is authenticated.
class LoginViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
    def test_login_successful(self):
        # Create a client and log in the user
        client = Client()
        response = client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
         # Check that the user is redirected to the correct page
        self.assertRedirects(response, reverse('rpds'))
         # Check that the user is logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)