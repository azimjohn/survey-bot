from django.contrib import admin
from django.urls import path
from bot.views import get_updates

urlpatterns = [
    path('', admin.site.urls),
    path('bot/get_updates/', get_updates),
]
