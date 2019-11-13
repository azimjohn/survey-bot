import jsonfield
from django.db import models


class Respondent(models.Model):
    user_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=128, blank=True)

    step = models.SmallIntegerField(default=0)
    details = jsonfield.JSONField(max_length=8192, default=dict)
