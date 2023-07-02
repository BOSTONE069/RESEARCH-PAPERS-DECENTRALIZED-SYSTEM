from logging import Logger
from django.shortcuts import render, redirect
from web3 import Web3
from django.http import HttpResponseRedirect
from .models import Contact
from django.core.exceptions import ValidationError
from .forms import ContactForm, ArticleForm
from django.utils.html import escape
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
# from django.utils.decorators import ratelimit
from django.conf import settings
import asyncio
from . import config
import requests
# contractAddress = 0x5B8609b04F00c48Abf9398da9D33E6DE097a6343
# walletAddress =   0x967D5De076f1cba86eA1723453a475d29CE708E7


# create a web3 object using the Infura endpoint
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

def Home(request):
    """
    The function "Home" returns a rendered HTML template called "index.html" when a request is made.

    :param request: The request parameter is an object that represents the HTTP request made by the
    client. It contains information such as the HTTP method (GET, POST, etc.), headers, user session,
    and any data sent in the request body
    :return: the rendered HTML template "rpds/index.html".
    """
    return render(request, "rpds/index.html")


def about(request):
    return render(request, "rpds/about.html")

def get_pinned_files():
    """
    The function `get_pinned_files` retrieves a list of pinned files from the Pinata API.
    :return: The function `get_pinned_files` returns a list of dictionaries containing information about
    pinned files. Each dictionary in the list includes the file name, IPFS hash, and the date it was
    pinned. If there is an error in retrieving the list of pinned files, a dictionary with an 'error'
    key will be returned.
    """
    pinata_api_url = 'https://api.pinata.cloud'
    endpoint = '/data/pinList?status=pinned'
    headers = {
        'Content-Type': 'application/json',
        'pinata_api_key': str(config.PINATA_API_Key),
        'pinata_secret_api_key': str(config.PINATA_API_Secret)
    }
    response = requests.get(
        f'{pinata_api_url}{endpoint}',
        headers=headers
    )
    data = response.json()

    files = []
    if response.status_code == 200:
        for item in data['rows']:
            file_info = {
                'name': item['metadata']['name'],
                'ipfs_hash': item['ipfs_pin_hash'],
                'date_pinned': item['date_pinned']
            }
            files.append(file_info)
    else:
        files.append({'error': 'Failed to get list of pinned files'})

    return files

def rpds_app(request):
    """
    The function `rpds_app` retrieves pinned files and renders the "rpds.html" template with the files
    as context.

    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method, headers, and any data sent with the
    request. It is typically passed to view functions in Django to handle the request and generate a
    response
    :return: The function `rpds_app` is returning a rendered HTML template called "rpds.html" with a
    context variable `files` that contains the result of the `get_pinned_files()` function.
    """
    files = get_pinned_files()

    return render(request, "rpds/rpds.html",  {'files': files})

def contact(request):
    """
    The `contact` function handles a POST request to save a contact form, and renders the contact form
    for a GET request.

    :param request: The request object represents the HTTP request that the user made to the server. It
    contains information such as the user's browser, IP address, and any data that was sent with the
    request
    :return: a rendered HTML template called 'rpds/contact.html' along with a dictionary containing the
    form object.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = Contact(name=name, email=email)
            contact.save()
            messages.success(request, "Your Email Address has been saved successfully")
            return redirect ("success")
    else:
        form = ContactForm()
    return render(request, 'rpds/contact.html', {'form': form})

def success(request):
    # Render the success.html template
    return render(request, 'rpds/success.html')

    # Redirect to the contact page after a delay
    # return redirect('contact')


def connect_metamask(request):
    web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

    # Check if MetaMask is installed and accessible
    if web3.is_connected():
        # Retrieve the user's accounts from MetaMask
        accounts = web3.eth.accounts

        # Process the accounts or perform other actions
        # Example: Print the first account
        if accounts:
            connected_account = accounts[0]
            print(connected_account)

            # Pass the connected account to the template
            return render(request, 'rpds/connect_metamask.html', {'connected_account': connected_account})
    else:
        # MetaMask is not available or not connected
        print("MetaMask not accessible")

        # You can display an error message or redirect to an error page
        return render(request, 'rpds/error.html', {'message': 'MetaMask not accessible'})

    return render(request, 'rpds/connect_metamask.html')


def login_view(request):
    """
    If the request method is POST, then validate the form and log the user in

    :param request: The current request object
    :return: The login.html page is being returned.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = escape(form.cleaned_data.get('username'))
            password = escape(form.cleaned_data.get('password'))
            user = authenticate(username=username, password=password)
            try:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('rpds')
                else:
                    messages.error(request, 'Invalid username or password')
            except Exception as e:
                Logger.error(f'Error during authentication: {str(e)}')
                messages.error(request, 'An error occurred during login')
    else:
        form = AuthenticationForm()
    return render(request, 'rpds/login.html', {'form': form})

# Fixed code with input validation

@csrf_protect
def register_view(request):
    """
    This function handles user registration, including form validation, password encryption, and
    authentication.

    :param request: The HTTP request object that contains information about the current request, such as
    the user's browser information, the requested URL, and any submitted data
    :return: a rendered HTML template 'rpds/register.html' with a form object as a context variable. If
    the request method is POST and the form is valid, the function creates a new user with the provided
    username and password, logs them in, and redirects them to the 'rpds' page. If the form is invalid
    or the user authentication fails, the function does not redirect and
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                password = form.cleaned_data.get('password')
                user = form.save(commit=False)
                user.password = make_password(password)
                user.save()
                username = form.cleaned_data.get('username')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('rpds')
                else:
                    # Handle invalid credentials
                    messages.error(request, 'Invalid credentials. Please try again.')
            except ValidationError:
                # Handle invalid inputs here
                messages.error(request, 'Invalid inputs. Please correct the errors and try again.')
    else:
        form = UserCreationForm()
    return render(request, 'rpds/register.html', {'form': form})

def logout_view(request):
    """
    Log out the current user and redirect to the login page

    :param request: The current request object
    :return: Redirects to the login page
    """
    logout(request)
    return redirect('login')

def article_create(request):
    """
    The function `article_create` is used to create a new article by handling a POST request, validating
    the form data, saving the article, and displaying a success message.

    :param request: The request object represents the HTTP request that the user made to the server. It
    contains information such as the HTTP method (GET, POST, etc.), headers, and any data sent with the
    request
    :return: a rendered HTML template called 'submit.html' with the form as a context variable.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Article has been saved successfully")
            return redirect ("success")
    else:
        form = ArticleForm()
    return render(request, 'rpds/submit.html', {'form': form})