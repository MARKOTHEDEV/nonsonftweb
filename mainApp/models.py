from calendar import c
from django.db import models
from  django.contrib.auth import get_user_model


class CvData(models.Model):
    name = models.CharField(max_length=300)
    english_qualification = models.CharField(max_length=300)
    country =models.TextField()

    def __str__(self):return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    message= models.TextField()

    def __str__(self):return f'{self.name} contacted us'



class Survey(models.Model):
    email  = models.TextField()
    discordID = models.TextField(null=True,)
    quetion = models.CharField(max_length=900)
    anser = models.TextField()
    country_time = models.CharField(max_length=300)


    def __str__(self):return f"{self.email} survey"
class Quetions(models.Model):
    name = models.CharField(max_length=900)

    def __str__(self): return f'quetion {self.id}'



class closeSurvey(models.Model):
    isOpen= models.BooleanField(default=False)

    def __str__(self):return 'Close assessment form'