import os

from django.db import models
from requests import get

class Post(models.Model):
    type = models.CharField(max_length=128, null=True, blank=True)
    language = models.CharField(blank=True, max_length=128, null=True)
    subject = models.CharField(max_length=128, null=True, blank=True)
    region = models.CharField(max_length=128, null=True, blank=True)
    district = models.CharField(max_length=128, null=True, blank=True)
    price = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)

    userid = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def publish(self):
        bot_token = os.environ.get("BOT_TOKEN")
        text = f"""type: {self.type}\nsubject: {self.subject}\nregion: {self.region}\ndistrict: {self.district}\nprice: {self.price}\nphone: {self.phone}\nusername: @{self.username}"""
        params = {
            "chat_id": "@ustoztop",
            "text": text
        }
        return get(f"https://api.telegram.org/bot{bot_token}/sendMessage", params=params)


    def __str__(self):
        return "{} - {} - {} - {}".format(self.pk, self.is_published, self.region, self.subject)


class StepInfo(models.Model):
    chat_id = models.IntegerField()
    user_id = models.IntegerField(null=True)
    username = models.CharField(blank=True, max_length=128, null=True)
    first_name = models.CharField(blank=True, max_length=128, null=True)
    last_name = models.CharField(blank=True, max_length=128, null=True)
    step = models.SmallIntegerField(default=0)

    language = models.CharField(blank=True, max_length=128, null=True)
    type = models.CharField(blank=True, max_length=128, null=True)
    subject = models.CharField(blank=True, max_length=128, null=True)
    region = models.CharField(blank=True, max_length=128, null=True)
    district = models.CharField(blank=True, max_length=128, null=True)
    price = models.CharField(blank=True, max_length=128, null=True)
    phone = models.CharField(blank=True, max_length=128, null=True)
