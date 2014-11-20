from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import UserProfile


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'password',
        )
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super().restore_object(attrs, instance)

        password = attrs.get('password', None)
        if password:
            user.set_password(password)

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', required=False)
    first_name = serializers.CharField(source='user.first_name',
                                       required=False)
    last_name = serializers.CharField(source='user.first_name', required=False)

    class Meta:
        model = UserProfile
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'tagline', 'created_at', 'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at',)

    def restore_object(self, attrs, instance=None):
        profile = super().restore_object(attrs, instance)

        if profile:
            user = profile.user
            user.email = attrs.get('user.email', user.email)
            user.first_name = attrs.get('user.first_name', user.first_name)
            user.last_name = attrs.get('user.last_name', user.last_name)
            user.save()

        return profile
