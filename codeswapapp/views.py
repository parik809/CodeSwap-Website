from django.shortcuts import render, redirect
from django.contrib import messages
from codeswapapp.models import Contact, ProductQuery

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        product = ProductQuery(name=name, email=email, message=message)
        product.save()

    return render(request, 'products.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        query = request.POST['query']

        contact = Contact(name=name, mobile=mobile, email=email, query=query)
        contact.save()

    return render(request, 'contact.html')
