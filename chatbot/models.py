from django.db import models

# Create your models here.


class ChatData(models.Model):
    sl = models.IntegerField(auto_created=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)
