from django.db import models


# Create your models here.

class BookInfos(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    bcommet = models.IntegerField(default=0)
    bread = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

class HeroInfos(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfos')
    isDelete = models.BooleanField(default=False)




