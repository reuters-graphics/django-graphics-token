from django.urls import include, path
from rest_framework import routers

from .viewsets import TokenGroupViewSet, TokenUserViewSet

router = routers.DefaultRouter()

router.register(r"token-users", TokenUserViewSet, basename="token-users")
router.register(r"token-groups", TokenGroupViewSet, basename="token-groups")

urlpatterns = [
    path("api/", include(router.urls)),
]
