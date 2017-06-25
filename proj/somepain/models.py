from django.db import models


class InitialText(models.Model):
    txt = models.TextField(max_length=500)
    offset = models.TextField(max_length=5)


class ChangedText(models.Model):
    txt = models.TextField(max_length=500)