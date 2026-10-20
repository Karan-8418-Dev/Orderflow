from django.urls import path,include
from rest_framework.routers import DefaultRouter
from orderflow.apps.catalog.views import Categoryviewset,Productviewset

app_name = "catalog"

router = DefaultRouter()
router.register(r"categories",Categoryviewset,basename="category")
router.register(r"products",Productviewset,basename= "products")

urlpatterns = [
    path("",include(router.urls))
]
