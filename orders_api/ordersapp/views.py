from .models import Orders
from .serializers import OrdersSerializer
from rest_framework import viewsets


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
