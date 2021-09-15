from django.db import models

# Create your models here.
class profile(models.Model):
    image = models.ImageField(upload_to='image')

class banerImage(models.Model):
    image = models.ImageField(upload_to='image')

class portfolio_image(models.Model):
    image = models.ImageField(upload_to='image')