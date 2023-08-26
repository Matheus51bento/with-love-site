from core.views import index, sorte
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('boa-sorte', sorte, name="sorte"),
]
