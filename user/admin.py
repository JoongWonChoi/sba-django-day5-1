from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'useremail')
    pass
admin.site.register(Users, UsersAdmin)

# Register your models here.
