from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from product.models import Product, Category
from product.serializers import ProductSerializer

from django.views import generic

from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

@csrf_exempt
def product_list_api(request):
    """
    POST: create product
    GET: List products
    :param request:
    """

    if request.method == 'GET':
        product_serializer = ProductSerializer(Product.objects.all(), many=True)
        return JsonResponse({'data': product_serializer.data}, status=200)
    elif request.method == 'POST':
        data = request.POST
        product_serializer = ProductSerializer(data=data)
        if product_serializer.is_valid():
            new_product = product_serializer.save()
            return JsonResponse({'new_product_id': new_product.id }, status=201)
        else:
            return JsonResponse({errors: product_serializer.errors}, status=400)
    else:
        return JsonResponse({}, status=405)


class ProductListApi(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()