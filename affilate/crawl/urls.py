from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crawl.views import MyExampleViewSet, ItemView

from .views import custom_redirect


urlpatterns = [
    path('', custom_redirect, name='custom_redirect'),
    path('items', ItemView.as_view),
]
