from rest_framework import serializers

from events.models import Event
from organisations.serializers import NestedOrganisationSerializer


class EventSerializer(serializers.ModelSerializer):
    organisations = NestedOrganisationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'