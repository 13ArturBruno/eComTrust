from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy

from users.models import UserProfile

admin.site.index_title = gettext_lazy('eComTrust Administração')

class UserProfileAdmin(UserAdmin):
    VERBOSE_NAME_PLURAL = 'Usuários'
    list_display = ['username', 'email', 'is_seller']
    search_fields = ['name']
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'cpf',
                'is_seller',
                'password1',
                'password2',
            )
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(Group)
