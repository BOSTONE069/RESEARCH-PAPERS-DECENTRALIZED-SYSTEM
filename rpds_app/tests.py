from django.test import TestCase, Client
from .models import Contact
from datetime import datetime
from .forms import ContactForm
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from unittest.mock import patch
from .views import get_pinned_files
# Create your tests here.

# The ContactTests class tests the creation and string representation of a Contact object.
class ContactTests(TestCase):
    def setUp(self):
        """
        The setUp function creates a Contact object with the name 'John Doe' and email 'john@mail.com'.
        """
        self.contact = Contact.objects.create(name='John Doe', email='john@mail.com')

    def test_contact_creation(self):
        """
        The function tests the creation of a contact object and checks if the name, email, and
        created_at attributes are set correctly.
        """
        self.assertEqual(self.contact.name, 'John Doe')
        self.assertEqual(self.contact.email, 'john@mail.com')
        self.assertIsInstance(self.contact.created_at, datetime)

    def test_string_representation(self):
        """
        The function tests the string representation of a contact object.
        """
        self.assertEqual(str(self.contact), 'john@mail.com John Doe {}'.format(self.contact.created_at))

# This is a test case for a Django view that tests whether the view uses a contact form, saves data
# for valid form submission, and does not save data for invalid form submission.
class ContactViewTestCase(TestCase):
     def setUp(self):
        """
        The setUp function sets up the necessary variables for testing the 'contact' URL with valid
        data.
        """
        self.url = reverse('contact')
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john@example.com'
        }

     def test_contact_view_should_use_contact_form(self):
        """
        The function tests whether the contact view uses the contact form.
        """
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], ContactForm)

     def test_contact_view_should_save_data_for_valid_form_submission(self):
        """
        The function tests if a valid form submission saves the data correctly and redirects to the
        success page.
        """
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.first().name, 'John Doe')
        self.assertEqual(Contact.objects.first().email, 'john@example.com')
        self.assertRedirects(response, reverse('success'))

     def test_contact_view_should_not_save_data_for_invalid_form_submission(self):
        """
        The function tests that invalid form submissions do not save data and display an error message.
        """
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

# class RegisterViewTest(TestCase):
#     def test_register_view_with_valid_form(self):
#         """
#         Test that a new user is created and authenticated when valid form data is submitted
#         """
#         url = reverse('register')
#         data = {
#             'username': 'testuser',
#             'password1': 'testpassword123',
#             'password2': 'testpassword123'
#         }
#         response = self.client.post(url, data)
#         self.assertRedirects(response, reverse('rpds'))
#         user = User.objects.get(username='testuser')
#         self.assertTrue(user.is_authenticated)
#     def test_register_view_with_invalid_form(self):
#         """
#         Test that the form displays errors when invalid form data is submitted
#         """
#         url = reverse('register')
#         data = {
#             'username': '',
#             'password1': '',
#             'password2': ''
#         }
#         response = self.client.post(url, data)
#         form = response.context['form']
#         self.assertFalse(form.is_valid())
#         self.assertContains(response, "This field is required.")
#     def test_register_view_with_existing_user(self):
#         """
#         Test that the form displays errors when a username that already exists is submitted
#         """
#         user = User.objects.create_user(username='existinguser', password='testpassword123')
#         url = reverse('register')
#         data = {
#             'username': 'existinguser',
#             'password1': 'testpassword123',
#             'password2': 'testpassword123'
#         }
#         response = self.client.post(url, data)
#         form = response.context['form']
#         self.assertFalse(form.is_valid())
#         self.assertContains(response, "A user with that username already exists.")



@pytest.fixture
class PinnedFilesTests(TestCase):
    def mock_response():
        return {
            "count": 1,
            "rows": [
                {
                    "date_pinned": "2021-10-01T10:00:00.000Z",
                    "ipfs_pin_hash": "QmXzUZ3L6k8ZjJ9q4wBvWU1Wx4EJF5RJdK9zH6V1s8Mvz1",
                    "metadata": {
                        "name": "test.txt"
                    }
                }
            ]
        }
    def test_get_pinned_files_success(mock_response):
        """
        This is a unit test for the `get_pinned_files()` function that checks if it returns the expected
        output when given a mock response with a status code of 200.

        :param mock_response: This is a parameter that represents the expected response from the mocked
        API call. It is used to simulate a successful API response and ensure that the function under
        test can handle the response correctly
        """
        with patch('my_module.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            expected_output = [
                {
                    'name': 'test.txt',
                    'ipfs_hash': 'QmXzUZ3L6k8ZjJ9q4wBvWU1Wx4EJF5RJdK9zH6V1s8Mvz1',
                    'date_pinned': '2021-10-01T10:00:00.000Z'
                }
            ]
            assert get_pinned_files() == expected_output
    def test_get_pinned_files_failure():
        """
        This is a unit test function that tests the failure scenario of the "get_pinned_files" function in
        the "my_module" module.
        """
        with patch('my_module.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            expected_output = [{'error': 'Failed to get list of pinned files'}]
            assert get_pinned_files() == expected_output
    def test_get_pinned_files_empty_list(mock_response):
        """
        This is a unit test for the `get_pinned_files()` function when the response count is 0.

        :param mock_response: It is a dictionary that represents a mock response from an API call. It
        contains a 'count' key that represents the number of pinned files in the response
        """
        mock_response['count'] = 0
        with patch('my_module.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            expected_output = []
            assert get_pinned_files() == expected_output
            
            
import unittest

class ConnectMetamaskTestCase(unittest.TestCase):
    def setUp(self):
        self.request = None

    def test_connect_metamask_with_connected_accounts(self):
        # Mock the is_connected function to return True
        web3.is_connected = lambda: True

        # Mock the eth.accounts property to return a list of accounts
        web3.eth.accounts = ['0x1234567890abcdef']

        # Call the connect_metamask function
        response = connect_metamask(self.request)

        # Assert that the response contains the connected account
        self.assertEqual(response.context['connected_account'], '0x1234567890abcdef')

    def test_connect_metamask_with_no_connected_accounts(self):
        # Mock the is_connected function to return True
        web3.is_connected = lambda: True

        # Mock the eth.accounts property to return an empty list
        web3.eth.accounts = []

        # Call the connect_metamask function
        response = connect_metamask(self.request)

        # Assert that the response does not contain any connected account
        self.assertNotIn('connected_account', response.context)

    def test_connect_metamask_when_metamask_unavailable(self):
        # Mock the is_connected function to return False
        web3.is_connected = lambda: False

        # Call the connect_metamask function
        response = connect_metamask(self.request)

        # Assert that the response redirects to the error page
        self.assertEqual(response.template_name, 'rpds/error.html')
        self.assertEqual(response.context['message'], 'MetaMask not accessible')

if __name__ == '__main__':
    unittest.main()