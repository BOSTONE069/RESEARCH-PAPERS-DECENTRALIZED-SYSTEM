from django.shortcuts import render


def Home(request):
    return render(request, "rpds/index.html")


def rpds_app(request):
    return render(request, "rpds/rpds.html")


def contact(request, contact_info):
    return render(request, "rpds/contact.html")
