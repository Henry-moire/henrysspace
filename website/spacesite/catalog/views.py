from django.shortcuts import render


# Create your views here.
def index(request):
    # Hello
    return render(request, 'index.html')


def login(request):
    # Hello
    return render(request, 'login.html')


def contact(request):
    # Hello
    return render(request, 'contact.html')


def aboutus(request):
    # Hello
    return render(request, 'aboutus.html')


def services(request):
    # Hello
    return render(request, 'services.html')
