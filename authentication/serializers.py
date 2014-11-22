from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        source='password', write_only=True, required=False
    )
    confirm_password = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        super().validate(attrs)

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Password mismatch')

        return attrs

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            # Username and email should not be updated
            attrs.pop('username', None)
            attrs.pop('email', None)

        password = attrs.pop('password', None)

        obj = super().restore_object(attrs, instance=instance)

        if password:
            obj.set_password(password)

        return obj

    def get_validation_exclusions(self, instance=None):
        exclusions = super().get_validation_exclusions(instance=instance)
        if instance:
            return exclusions + ['email', 'username',]
        else:
            return exclusions

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'tagline', 'created_at', 'updated_at', 'password',
                  'confirm_password',)
        read_only_fields = ('id', 'created_at', 'updated_at',)
