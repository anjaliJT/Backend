from rest_framework import serializers
from django.contrib.auth.models import User
from .models import KBEntry

class RegisterSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'company_name']
        extra_kwargs = {'password': {'write_only': True}}


class KBEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = KBEntry
        fields = ['id', 'question', 'answer', 'category']

