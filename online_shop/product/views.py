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

class ProductDetailView(generic.DetailView):
    model = Product
    fields = "__all__"
    template_name = "product/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = Category
    fields = "__all__"
    template_name = "product/category_list.html"
