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
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "customer/register.html", {"form":form})


class CustomerLoginView(LoginView):
    template_name = 'customer/loginview_form.html'


def home(request):
    return render(request, "home.html")


#class Register(CreateView):
#    template_name = 'customer/register.html'
#    success_url = reverse_lazy('login')
#    form_class = RegisterForm
#    success_message = "Your profile was created successfully"


from customer.permissions import CustomerPermission
from customer.serializer import CustomerSerializer, AddressSerializer
from rest_framework import mixins, generics, authentication
from rest_framework.decorators import APIView
from rest_framework import permissions
from customer.models import Customer, Address


class CustomerListApi(APIView):
    def get(self, request):
        customer_serializer = CustomerSerializer(Customer.objects.all(), many=True)
        return Response(customer_serializer.data, status=200)

    def post(self, request):
        customer_serializer = CustomerSerializer(data=request.POST)
        if cutomer_serializer.is_valid():
            new_customer = customer_serializer.save()
            return Response({'new_customer_id': new_customer.id}, status=201)
        else:
            return Response({'errors': customer_serializer.errors}, status=400)


class AddressListApi(APIView):
    def get(self, request):
        address_serializer = AddressSerializer(Address.objects.all(), many=True)
        return Response(address_serializer.data, status=200)

    def post(self, request):
        address_serializer = AddressdSerializer(data=request.POST)
        if address_serializer.is_valid():
            new_address = address_serializer.save()
            return Response({'new_address': new_address}, status=201)
        else:
            return Response({'errors': address_serializer.errors}, status=400)


class CustomerDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, CustomerPermission]
    authentication_classes = [authentication.TokenAuthentication]