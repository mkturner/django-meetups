# Import dependencies from django
from django.urls import path

# Import dependencies from app
from . import views


urlpatterns = [
    path("meets/", views.index, name="meets"), # <domain>.com/meets/
]
