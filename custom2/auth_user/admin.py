# from django.contrib import admin

# from auth_user.models import User

# admin.site.register(User)

# from auth_user.models import User

# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.admin import UserAdmin
# from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.contrib import admin

# class UserCreationFormExtended(UserCreationForm): 
#     def __init__(self, *args, **kwargs): 
#         super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
#         self.fields['username'] = forms.CharField(label=_("Username"), max_length=75)

# UserAdmin.add_form = UserCreationFormExtended
# UserAdmin.add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('username', 'password1', 'password2',)
#     }),
# )

# # admin.site.unregister(User)
# admin.site.register(User, UserAdmin)




from auth_user.models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2'),
        }),
    )

admin.site.register(User, UserAdmin)