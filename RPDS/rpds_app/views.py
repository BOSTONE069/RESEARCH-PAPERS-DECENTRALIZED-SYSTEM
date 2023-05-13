from django.shortcuts import render
from web3 import Web3

# create a web3 object using the Infura endpoint
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/GUwpQv7dGLI2Ba4ecDTplOZmw2ubB2ue'))


def Home(request):
    return render(request, "rpds/index.html")


def about(request):
    return render(request, "rpds/about.html")


def rpds_app(request):
    return render(request, "rpds/rpds.html")


def contact(request):
    return render(request, "rpds/contact.html")
