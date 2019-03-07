from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        if 'password' in data:
            data['password'] = make_password(data['password'])
        return super(UserSerializer, self).to_internal_value(data)

    class Meta:
        model = UserProfile
        fields = ('email', 'password')
