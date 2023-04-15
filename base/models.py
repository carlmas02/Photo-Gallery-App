from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=20)
    # photo = models.ImageField(upload_to='pics')
    photo = CloudinaryField('image')