from django.urls import path
from customer.views import contact, CustomerLoginView, register

urlpatterns = [
    path('comment/', contact, name='contact'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('register/', register, name="register")
]
