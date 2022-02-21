from django.urls import path
from customer.views import contact

urlpatterns = [
    path('comment/', contact, name='contact')
]
