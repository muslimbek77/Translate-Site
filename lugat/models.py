from django.db import models


class Lugat(models.Model):
    inglizcha = models.CharField('Ingilizcha', max_length=30)
    uzbekcha = models.CharField('O\'zbekcha', max_length=30)