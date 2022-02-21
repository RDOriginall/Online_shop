from rest_framework import serializers
from product.models import Product, Category


# class ProductSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField(max_length=30)
#    brand = serializers.CharField(max_length=30)
#    price = serializers.IntegerField()
#    image = serializers.ImageField(allow_null=True)
#    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

#    def update(self, instanse: Product, validation_data: dict) -> Product:
#        instance.name = validated_data.get('name', instanse.name_en)
#        instance.brand = validated_data.get('brand', instanse.brand_en)
#        instance.price = validated_data.get('price', instanse.price)
#        instanse.image = validated_data.get('image', instanse.image)
#        instanse.category = validated_data.get('category', instanse.category)
#        return instanse

#    def create(self, validated_data: dict) -> Product:
#        return Product.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'