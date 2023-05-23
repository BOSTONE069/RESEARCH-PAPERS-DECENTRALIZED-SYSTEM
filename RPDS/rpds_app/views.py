from logging import Logger
from django.shortcuts import render, redirect
from web3 import Web3
from django.http import HttpResponseRedirect
from .models import Contact
from django.core.exceptions import ValidationError
from .forms import ContactForm
from django.utils.html import escape
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
# from django.utils.decorators import ratelimit
from django.conf import settings
import asyncio

# contractAddress = 0x5B8609b04F00c48Abf9398da9D33E6DE097a6343
# walletAdress =   0x967D5De076f1cba86eA1723453a475d29CE708E7



# create a web3 object using the Infura endpoint
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

def Home(request):
    return render(request, "rpds/index.html")


def about(request):
    return render(request, "rpds/about.html")


def rpds_app(request):

    return render(request, "rpds/rpds.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contact = Contact(email=email)
            contact.save()
            messages.success(request, "Your Email Address has been saved successfully")
            return redirect ("success")
    else:
        form = ContactForm()
    return render(request, 'rpds/contact.html', {'form': form})

def success(request):
    return render(request, 'rpds/success.html')


def connect_metamask(request):
    if request.method == 'POST':
        # Check if MetaMask is installed and accessible
        if Web3.isConnected():
            # Create a Web3 instance connected to the user's MetaMask provider
            web3 = Web3(Web3.WebsocketProvider(Web3.currentProvider))

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
# @ratelimit(key='user', rate='5/h', block=True)
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