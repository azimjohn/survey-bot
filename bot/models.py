import jsonfield
from django.db import models
from django.utils.html import format_html


class Respondent(models.Model):
    user_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    username = models.CharField(max_length=128, blank=True)

    @property
    def completed_responses_count(self):
        return self.responses.filter(completed=True).count()


class Response(models.Model):
    step = models.SmallIntegerField(default=0)
    details = jsonfield.JSONField(max_length=8192, default=dict)
    respondent = models.ForeignKey(Respondent, related_name="responses", on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    @property
    def html(self):
        table = "<table class='table'>"

        for question in self.details:
            answer = self.details[question]
            table += f"""
                <tr>
                    <td>{question}</td>
                    <td><b>{answer}</b></td>
                </tr>
            """

        table += "</table>"
        return format_html(table)
