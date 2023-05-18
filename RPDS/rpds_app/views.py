from django.shortcuts import render, redirect
from web3 import Web3
from django.http import HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
import asyncio

# create a web3 object using the Infura endpoint
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

def Home(request):
    return render(request, "rpds/index.html")


def about(request):
    return render(request, "rpds/about.html")


def rpds_app(request):
      # Create an instance of the Web3 class
    w3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))

     # Check if MetaMask is connected
    connected = False
    account = None
    try:
        if w3.eth.accounts:
            connected = True
            account = w3.eth.accounts[0]  # Get the first account
    except Exception as e:
        # Handle any exception that may occur when accessing eth.accounts
        print(f"Error occurred: {str(e)}")
    return render(request, "rpds/rpds.html", {'connected': connected, 'account': account})

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
    return render(request, 'rpds/connect_metamask.html')
