from graphics_token.models import TokenGroup, TokenUser
from rest_framework import serializers


class TokenGroupSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return [f"{perm.content_type.app_label}.{perm.codename}" for perm in obj.permissions.all()]

    class Meta:
        model = TokenGroup
        fields = ["name", "permissions"]


class TokenUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenUser
        fields = ["id", "name"]


class TokenUserSerializer(serializers.ModelSerializer):
    token_groups = TokenGroupSerializer(many=True, read_only=True)

    class Meta:
        model = TokenUser
        fields = ["id", "name", "token_groups"]
