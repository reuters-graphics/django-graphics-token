import uuid

from django.contrib import admin

from graphics_token.models import TokenGroup, TokenUser


def regenerate_token(modeladmin, request, queryset):
    for app in queryset:
        app.token = uuid.uuid4().hex[:30]
        app.save()


regenerate_token.short_description = "Regenerate app tokens"


class TokenUserAdmin(admin.ModelAdmin):
    fields = ("name", "token", "token_groups")
    readonly_fields = ("token",)
    list_display = (
        "name",
        "token",
    )
    search_fields = ("name",)
    list_filter = (("token_groups", admin.RelatedOnlyFieldListFilter),)
    actions = (regenerate_token,)


class TokenGroupAdmin(admin.ModelAdmin):
    fields = ("name", "permissions")
    filter_horizontal = ("permissions",)


admin.site.register(TokenUser, TokenUserAdmin)
admin.site.register(TokenGroup, TokenGroupAdmin)
