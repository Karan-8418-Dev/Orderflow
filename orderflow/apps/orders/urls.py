from django.urls import path,include
from orderflow.apps.orders.views import OrderItemViewset,OrderViewset
from rest_framework.routers import DefaultRouter
app_name = "orders"
router = DefaultRouter()
router.register(r"orders",OrderViewset,basename="orders")
router.register(r"order_items",OrderItemViewset,basename= "order_items")
urlpatterns = [
    # Order endpoints
     path("",include(router.urls))
]
