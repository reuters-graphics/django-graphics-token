from graphics_token.authentication import TokenAuthentication
from graphics_token.models import TokenGroup
from graphics_token.permissions import TokenModelPermissions
from graphics_token.serializers import TokenGroupListSerializer, TokenGroupSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class TokenGroupViewSet(ReadOnlyModelViewSet):
    serializer_class = TokenGroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (TokenModelPermissions,)
    pagination_class = None
    queryset = TokenGroup.objects.all()

    def list(self, request):
        queryset = TokenGroup.objects.all()
        serializer = TokenGroupListSerializer(queryset, many=True)
        return Response(serializer.data)
