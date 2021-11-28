from django.contrib import admin
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from .models import *


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
    }


admin.site.register(Person, CommentAdmin)