from rest_framework import serializers

from authentication.serializers import AccountSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(required=False)

    def get_valiation_exclusion(self, *args, **kwargs):
        exclusions = super().get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
