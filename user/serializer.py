from rest_framework import serializers
from .models import UserForm1, UserForm2


class UserForm1Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm1
        fields = '__all__'


class UserForm2Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm2
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    text = serializers.CharField()
