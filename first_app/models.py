from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name=models.CharField(max_length=100)

    def __str__(self):
        return self.top_name


class webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.PROTECT)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        self.name


class accessRecord(models.Model):

    name=models.ForeignKey(webpage,on_delete=models.PROTECT)
    date=models.DateField()

    def __str__(self):
        return str(self.date)


