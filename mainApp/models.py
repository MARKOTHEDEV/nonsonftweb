from django.db import models



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