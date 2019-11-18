from django.contrib import admin
from .models import Respondent

admin.site.site_header = 'SurveyBot Admin'


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username")
    fields = ("first_name", "last_name", "username",)
    list_display = ("first_name", "last_name", "username",)
    readonly_fields = ("first_name", "last_name", "username",)
