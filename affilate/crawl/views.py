from django.shortcuts import redirect, render
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_csv.renderers import CSVRenderer

from affilate import settings
from .models import Item
from .serializers import ItemSerializer


def custom_redirect(request):
    if request.user.is_authenticated:
        # Redirect to the admin page or any other page you want
        return redirect('admin:index')  # Replace 'admin:index' with your desired URL
    else:
        # Render your login page
        return render(request, 'html_regex.html')


class APIPermission(IsAuthenticatedOrTokenHasScope):
    def has_permission(self, request, view):
        if settings.DEBUG:
            view.auth_permission = True
            return True

        ret = super().has_permission(request, view)
        if request.user and request.user.is_authenticated:
            return request.user.is_staff
        else:
            view.auth_permission = ret

        return ret


class BaseCSVRenderer(CSVRenderer):
    header = ['id', 'discount', 'image_link', 'item_link', 'mrp', 'name', 'price']


class MyExampleViewSet(XLSXFileMixin, ReadOnlyModelViewSet):
    renderer_classes = ReadOnlyModelViewSet.renderer_classes + [XLSXRenderer, BaseCSVRenderer]

    def get_renderer_context(self):
        return super().get_renderer_context()


class ItemView(MyExampleViewSet, RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filename = 'my_export.xlsx'
