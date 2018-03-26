from django.db import models

# Create your models here.

class areas(models.Model):
    area = models.CharField(max_length=20)
    parea = models.ForeignKey("self",null=True,blank=True)
    class Meta():
        db_table = "areas"
    def __str__(self):
        return self.area