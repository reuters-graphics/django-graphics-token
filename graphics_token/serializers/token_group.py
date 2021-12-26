from graphics_token.models import TokenGroup, TokenUser
from rest_framework import serializers


class TokenUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenUser
        fields = ["id", "name"]


class TokenGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenGroup
        fields = ["id", "name"]


class TokenGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()
    token_users = TokenUserSerializer(many=True, read_only=True)

    def get_permissions(self, obj):
        return [f"{perm.content_type.app_label}.{perm.codename}" for perm in obj.permissions.all()]

    class Meta:
        model = TokenGroup
        fields = ["id", "name", "permissions", "token_users"]
