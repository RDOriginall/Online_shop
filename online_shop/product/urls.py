from django.urls import path

from product.apis import *
from product.views import *


urlpatterns = [
    path('product_list_api/', product_list_api, name='product_list_api'),
    path('product_api/', ProductListApi.as_view(), name='product_list_api'),
    path('product_api/<int:pk>', ProductDetailApi.as_view(), name='product_api'),
    path('category_api/', CategoryListApi.as_view(), name='category_list_api'),
    path('category_api/<int:pk>', CategoryListApi.as_view(), name='category_list_api'),
    path('products', ProductListView.as_view(), name='products'),
    path('category', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name="ProductDetailView"),
]
