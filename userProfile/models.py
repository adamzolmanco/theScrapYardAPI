from django.db import models

# Create your models here.
class UserProfile(models.Model):
    id=models.AutoField(primary_key=True)
    token= models.TextField()
    walletLoc = models.TextField()
