from rest_framework import serializers

from users.models import CustomUser


class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email']
