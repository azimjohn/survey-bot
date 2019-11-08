import jsonfield
from django.db import models


class Respondent(models.Model):
    name = models.CharField(max_length=128, blank=True)
    user_id = models.IntegerField(null=True)
    step = models.SmallIntegerField(default=0)
    username = models.CharField(blank=True, max_length=128)

    details = jsonfield.JSONField(max_length=8192, default=dict)
