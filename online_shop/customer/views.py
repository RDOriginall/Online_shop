from django.shortcuts import render, redirect
from customer.forms import ContactForm
from customer.models import Customer
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from customer.forms import RegisterForm

"""
def create_message(request):
    messages.set_level(request, 0)
    messages.add_message(request, messages.ERROR, "Invalid input!")
    messages.info(request, "Please fill up the fields")
    messages.success(request, "Your comment added successfully")
    messages.warning(request, "This filed can't be empty")
    return HttpResponse("New messages created!")
"""


def contact(request):
    if request.method == 'POST':
        messages.set_level(request, 0)
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your comment added successfully!")
            return HttpResponse("New comment sent successfully")
        else:
            messages.warning(request, "Field is empty or contains invalid input!")
            return HttpResponse("Please try again!")


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("customer/lognview_form.html")
    else:
        form = RegisterForm()

    return render(response, "customer/register.html", {"form":form})


class CustomerLoginView(LoginView):
    template_name = 'customer/loginview_form.html'

