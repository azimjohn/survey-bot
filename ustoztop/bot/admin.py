from django.contrib import admin
from .models import Post

admin.site.site_header = 'UstozTop Administration'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def publish(modelAdmin, request, queryset):
        for post in queryset:
            post.publish()
        queryset.update(is_published=True)


    publish.short_description = 'Publish to @ustoztop channel'

    list_display = (
        'id',
        'type',
        'subject',
        'region',
        'price',
        'phone',
        'is_published'
    )
    actions = [publish,]

