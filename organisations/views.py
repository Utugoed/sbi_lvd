from django.shortcuts import render

from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from organisations.models import Organisation
from organisations.serializers import OrganisationSerializer


class OrganisationsViewSet(CreateModelMixin, GenericViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = (IsAuthenticated,)