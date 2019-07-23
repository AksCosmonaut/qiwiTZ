from django.urls import path, include

from rest_framework import routers
from .views import OrdersViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrdersViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
