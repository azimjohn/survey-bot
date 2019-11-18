from django.contrib import admin
from .models import Respondent, Response

admin.site.site_header = 'SurveyBot Admin'


class ResponseInline(admin.StackedInline):
    model = Response
    max_num = 0
    can_delete = False
    fields = ("html",)
    readonly_fields = ("html",)


@admin.register(Respondent)
class RespondentAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username")
    fields = ("first_name", "last_name", "username", "completed_responses_count")
    list_display = ("first_name", "last_name", "username", "completed_responses_count")
    readonly_fields = ("first_name", "last_name", "username", "completed_responses_count")
    list_select_related = ("responses",)
    inlines = (ResponseInline,)
