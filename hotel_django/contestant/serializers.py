from rest_framework import serializers
from .models import Contestant
from django.contrib.auth.hashers import make_password

class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contestant
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "registration_date",
        )
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        contestant = Contestant.objects.create(**validated_data)
        return contestant
