from django.urls import path,include
from orderflow.apps.payments.views import PaymentHistoryViewset
from rest_framework.routers import DefaultRouter
app_name = "payments"
router = DefaultRouter()

router.register(r"payment_history",PaymentHistoryViewset,basename="payment")
urlpatterns = [
    # Payment endpoints
    path("",include(router.urls))
]
