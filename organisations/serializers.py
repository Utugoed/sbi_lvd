from rest_framework import serializers

from organisations.models import Organisation
from users.serializers import NestedUserSerializer


class OrganisationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organisation
        fields = '__all__'


class NestedOrganisationSerializer(serializers.ModelSerializer):
    users = NestedUserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Organisation
        fields = ['id', 'title', 'description', 'full_address', 'users']
    