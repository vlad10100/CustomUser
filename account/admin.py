from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm


from account.models import CustomUser

class UserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email','username')


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, UserAdmin)