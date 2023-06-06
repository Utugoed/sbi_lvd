from django_filters import rest_framework as django_filters

from rest_framework import filters, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from events.models import Event
from events.serializers import EventSerializer


class CustomDateFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date_gt = request.query_params.get('date_gt')
        date_lt = request.query_params.get('date_lt')
        if date_gt:
            queryset = queryset.filter(date__gt=date_gt)
        if date_lt:
            queryset = queryset.filter(date__lt=date_lt)
        return queryset


class EventPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EventsViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = Event.get_queryset()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated, )

    filter_backends = [
        CustomDateFilter,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ['date']
    ordering_fields = ["date"]
    search_fields = ['title']

    pagination_class = EventPagination
