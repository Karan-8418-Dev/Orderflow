from django.urls import path
from orderflow.apps.users.views import Registerview,Profileview

app_name = "users"

urlpatterns = [
    # User and authentication endpoints
    path("register/",Registerview.as_view(),name="registers"),
    path("me/",Profileview.as_view(),name = "profile"),
]
