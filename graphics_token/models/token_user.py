import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.itercompat import is_iterable

from .token_group import TokenGroup


class TokenUser(AbstractBaseUser):
    name = models.SlugField(max_length=100, unique=True)
    token = models.SlugField(max_length=30, unique=True, editable=False)
    password = None
    last_login = None
    token_groups = models.ManyToManyField(
        TokenGroup,
        related_name="token_users",
        related_query_name="token_user",
    )

    USERNAME_FIELD = "name"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex[:30]
        super().save(*args, **kwargs)

    def has_perms(self, perm_list, obj=None):
        if not is_iterable(perm_list) or isinstance(perm_list, str):
            raise ValueError("perm_list must be an iterable of permissions.")
        return all(self.has_perm(perm, obj) for perm in perm_list)

    def has_perm(self, perm, obj=None):
        all_perm_codes = []
        for token_group in self.token_groups.all():
            for perm_code in token_group.get_all_perm_codes():
                all_perm_codes.append(perm_code)
        return perm in all_perm_codes
