from django.urls import path
from customer.views import contact, CustomerLoginView, register, home

urlpatterns = [
    path('comment/', contact, name='contact'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('register/', register, name="register"),
    path('home/', home, name="home")
]
