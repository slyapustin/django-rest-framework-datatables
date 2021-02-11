from django_filters import rest_framework as filters
from rest_framework_datatables.django_filters.filters import GlobalFilter

from albums.models import Album


class GlobalDateFilter(GlobalFilter, filters.DateFilter):
    pass


class CustomAlbumGlobalFilter(filters.FilterSet):
    created_on = GlobalDateFilter(field_name="created_on__date", lookup_expr='exact')

    class Meta:
        model = Album
        fields = ['created_on']


class CustomAlbumFilter(filters.FilterSet):
    created_on = filters.DateFilter(field_name="created_on__date", lookup_expr='exact')

    class Meta:
        model = Album
        fields = ['created_on']
