from .views import index, treatment
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('treatment/', treatment, name='checkForm'),
]
