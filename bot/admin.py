from django.contrib import admin
from .models import Respondent

admin.site.site_header = 'SurveyBot Admin'


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "step")
    search_fields = ("first_name", "last_name", "username")
