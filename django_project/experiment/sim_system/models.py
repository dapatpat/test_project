from django.db import models

# Create your models here.

class stuInfos(models.Model):
    stu_no = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=30)
    stu_gender = models.BooleanField()
    stu_duty = models.CharField(max_length=30,null=True)
    stu_age = models.IntegerField()
    # sub_score = models.FloatField()
    # sub_no = models.ForeignKey("subInfos")
    class Meta():
        db_table = "stuInfos"

class subInfos(models.Model):
    sub_no = models.IntegerField(primary_key=True,auto_created=True)
    sub_name = models.CharField(max_length=10)
    class Meta():
        db_table = 'subInfos'