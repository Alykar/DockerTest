from django.db import models


class Message(models.Model):

    text = models.TextField(max_length=1000)
    name = models.TextField(max_length=100, default="someName")