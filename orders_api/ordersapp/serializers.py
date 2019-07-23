from .models import Orders
from rest_framework import serializers


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ("id", "description", "price")
