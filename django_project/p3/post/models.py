from django.db import models


# Create your models here.

class des(models.Model):
    text = models.TextField()

    class Meta():
        db_table = "des"
