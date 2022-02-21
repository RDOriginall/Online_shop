from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View

from product.models import Product, Category
from product.serializers import ProductSerializer

from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    fields = '__all__'
    template_name = 'product/product_list.html'