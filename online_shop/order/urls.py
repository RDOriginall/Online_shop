from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.views import *


router = DefaultRouter()
router.register('OrderItem', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
