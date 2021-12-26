import uuid

from django.contrib.auth.models import Permission
from django.db import models


class TokenGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.SlugField(max_length=100, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        related_name="token_groups",
        related_query_name="token_group",
    )

    def get_all_perm_codes(self):
        return [f"{p.content_type.app_label}.{p.codename}" for p in self.permissions.all()]

    def __str__(self):
        return self.name
