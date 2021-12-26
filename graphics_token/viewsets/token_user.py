from graphics_token.authentication import TokenAuthentication
from graphics_token.models import TokenUser
from graphics_token.permissions import TokenModelPermissions
from graphics_token.serializers import TokenUserListSerializer, TokenUserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class TokenUserViewSet(ReadOnlyModelViewSet):
    serializer_class = TokenUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (TokenModelPermissions,)
    pagination_class = None
    queryset = TokenUser.objects.all()

    def list(self, request):
        queryset = TokenUser.objects.all()
        serializer = TokenUserListSerializer(queryset, many=True)
        return Response(serializer.data)
